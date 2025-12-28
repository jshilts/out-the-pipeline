# -*- coding: utf-8 -*-
# > cd "C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline"
# >  .\.venv\Scripts\activate
# then set  Tools>Preferences>Python Intepreter  to  C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline\.venv\Scripts\python.exe

import sys
import re
import random
from time import sleep
from pathlib import Path
from urllib.parse import urlparse, urljoin
from datetime import datetime
from typing import Optional, Tuple, List

from bs4 import BeautifulSoup, Tag, NavigableString


try:
    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeoutError
except Exception:
    raise SystemExit("playwright is required. Install with:\n  pip install playwright\n  playwright install")

try:
    from dateutil import parser as dateparser
except Exception:
    dateparser = None

# ----------- Config ------------
UA_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]
DEFAULT_WAIT_MIN = 2.0
DEFAULT_WAIT_MAX = 6.0
OUT_DIR = Path("./webarticles/").resolve()

# ---------- Utilities ----------
def wait_random(min_sec=DEFAULT_WAIT_MIN, max_sec=DEFAULT_WAIT_MAX):
    sleep(random.uniform(min_sec, max_sec))

def looks_like_cloudflare(content: Optional[str], url: Optional[str]) -> bool:
    if not content:
        return False
    u = (url or "").lower()
    if "cloudflare.com" in u:
        return True
    c = content.lower()
    phrases = ["checking your browser", "just a moment", "please enable javascript", "cf-chl-bypass"]
    return any(p in c for p in phrases)

def slugify_path_from_url(url: str) -> str:
    p = urlparse(url).path
    last = p.rstrip("/").split("/")[-1] or "page"
    last = re.sub(r"\.[a-zA-Z0-9]+$", "", last)
    last = re.sub(r"[^a-zA-Z0-9\-]+", "-", last)
    last = re.sub(r"-{2,}", "-", last).strip("-").lower()
    return last or "page"

def parse_date_string(ds: Optional[str]) -> Optional[datetime]:
    if not ds:
        return None
    ds = ds.strip()
    try:
        if ds.endswith("Z"):
            return datetime.fromisoformat(ds.replace("Z", "+00:00"))
        return datetime.fromisoformat(ds)
    except Exception:
        pass
    if dateparser:
        try:
            return dateparser.parse(ds)
        except Exception:
            pass
    fmts = ["%d %b %Y %I:%M %p", "%d %b %Y", "%b %d, %Y", "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%d %H:%M:%S", "%B %d, %Y", "%d %B %Y"]
    for f in fmts:
        try:
            return datetime.strptime(ds, f)
        except Exception:
            continue
    return None

def filename_from_date_and_slug(dt: Optional[datetime], slug: str) -> str:
    if dt:
        name = dt.strftime("%Y%m%d") # dt.strftime("%Y%b%d")  # %b gives month as Dec instead of number 12
    else:
        name = "YYYYMMDD"#datetime.utcnow().strftime("%Y%m%d")
    return f"{name}-{slug}"

def ensure_unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    base = path.stem
    suf = path.suffix
    counter = 1
    while True:
        candidate = path.with_name(f"{base}-{counter}{suf}")
        if not candidate.exists():
            return candidate
        counter += 1

# ---------- Extraction (unchanged logic, packaged) ----------
def first_text_from_selectors(soup: BeautifulSoup, selectors):
    for sel in selectors:
        el = soup.select_one(sel)
        if el and el.get_text(strip=True):
            return el.get_text(strip=True)
    return None

_DATE_REGEX = re.compile(r'\b\d{1,2}\s+[A-Za-z]{3,9}\s+\d{4}\b')  # e.g. "4 Sep 2025"
def extract_pubdate_from_soup(soup):
    """
    Extract the publish date from <span class="news-article__hero__date"> elements.
    Returns a string like "4 Sep 2025", or None if not found.
    """
    date_spans = soup.select(".news-article__hero__date")
    for span in date_spans:
        text = span.get_text(strip=True)
        # match day month year pattern, e.g., 4 Sep 2025
        if re.match(r"\d{1,2}\s+[A-Za-z]{3,9}\s+\d{4}", text):
            return text
    return None
    

def extract_article_fields_from_html(html: str, base_url: Optional[str] = None) -> dict:
    soup = BeautifulSoup(html, "html.parser")        
    
    pub_date_raw = extract_pubdate_from_soup(soup)  # must extract date before decompose() gets rid of all the stuff under 'script'
    pub_dt = parse_date_string(pub_date_raw) if pub_date_raw else None

    
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    title = ""
    meta_og = soup.find("meta", property="og:title")
    if meta_og and meta_og.get("content"):
        title = meta_og["content"].strip()
    if not title:
        meta_title = soup.find("meta", attrs={"name": "title"})
        if meta_title and meta_title.get("content"):
            title = meta_title["content"].strip()
    if not title:
        title_el = (soup.select_one("article h1")
                    or soup.select_one("h1[itemprop='headline']")
                    or soup.select_one("h1"))
        if title_el:
            title = title_el.get_text(strip=True)

    category = ""
    meta_section = soup.find("meta", property="article:section")
    if meta_section and meta_section.get("content"):
        category = meta_section["content"].strip()
    if not category:
        category = first_text_from_selectors(
            soup,
            [".kicker", ".eyebrow", ".article-kicker", ".c-article__kicker",
             ".article__kicker", ".topic", ".section", ".article-genre", ".blog-genre"]
        ) or ""
    if not category:
        top_link = soup.select_one("a.section, a.topic, .kicker a, .eyebrow a")
        if top_link:
            category = top_link.get_text(strip=True)
    
    candidates = [
        soup.find("article"),
        soup.select_one(".article-body"),
        soup.select_one(".article__body"),
        soup.select_one(".c-article__body"),
        soup.select_one(".article-content"),
        soup.select_one("#content"),
        soup.select_one("div[itemprop='articleBody']"),
        soup.select_one("main"),
    ]
    body_el = None
    for cand in candidates:
        if cand and isinstance(cand, (Tag, BeautifulSoup)):
            if cand.find("p") or cand.find("div"):
                body_el = cand
                break
    if not body_el:
        divs = soup.find_all("div")
        best, best_p = None, 0
        for d in divs:
            p_count = len(d.find_all("p"))
            if p_count > best_p:
                best_p = p_count
                best = d
        if best_p >= 1:
            body_el = best

    article_html = ""
    article_text = ""
    if body_el:
        for rm_sel in [".related-articles", ".newsletter-signup", ".share", ".author-bio", ".comments", ".ad", ".ads"]:
            for rm in body_el.select(rm_sel):
                rm.decompose()

        if base_url:
            for a in body_el.find_all("a", href=True):
                href = a["href"]
                if href.startswith("/"):
                    a["href"] = urljoin(base_url, href)

        article_html = "".join(str(child) for child in body_el.contents).strip()

        parts = []
        for elem in body_el.descendants:
            if isinstance(elem, NavigableString):
                if getattr(elem, "parent", None) is not None and getattr(elem.parent, "name", "").lower() == "a":
                    continue
                text = str(elem).strip()
                if text:
                    parts.append(text)
            elif isinstance(elem, Tag) and elem.name == "a" and elem.get_text(strip=True):
                href = elem.get("href", "").strip()
                link_text = elem.get_text(strip=True)
                if href:
                    parts.append(f"{link_text} ({href})")
                else:
                    parts.append(link_text)
            elif isinstance(elem, Tag) and elem.name in ("p", "br"):
                parts.append("\n")
        joined = " ".join(p for p in parts)
        joined = re.sub(r"[ \t\f\v]+", " ", joined)
        joined = re.sub(r"(?:\n\s*){2,}", "\n\n", joined).strip()
        article_text = joined

    return {
        "title": title or "",
        "category": category or "",
        "published_raw": pub_date_raw or "",
        "published_dt": pub_dt,
        "article_html": article_html or "",
        "article_text": article_text or "",
    }

# ---------- Playwright fetching (reused browser) ----------
def fetch_rendered_html_polite_with_browser(p, browser, url: str, headful_fallback=True, timeout=60000) -> Tuple[str, str]:
    """
    Use a provided (headless) browser to create a new context for the URL.
    If Cloudflare-like challenge detected, optionally run a headful fallback for this single URL.
    Returns (content, final_url).
    """
    ua = random.choice(UA_LIST)
    context = browser.new_context(user_agent=ua, locale="en-US")
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    context.set_extra_http_headers({"accept-language": "en-US,en;q=0.9", "referer": url})
    page = context.new_page()
    content = ""
    final_url = url
    try:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=timeout)
        except PWTimeoutError:
            pass
        sleep(random.uniform(1.2, 3.4))
        content = page.content()
        final_url = page.url
        if looks_like_cloudflare(content, final_url) and headful_fallback:
            # close context and try short-lived headful browser to attempt challenge solve
            try:
                context.close()
            except Exception:
                pass
            headful_browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
            try:
                ctx2 = headful_browser.new_context(user_agent=ua, locale="en-US")
                ctx2.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
                ctx2.set_extra_http_headers({"accept-language": "en-US,en;q=0.9", "referer": url})
                page2 = ctx2.new_page()
                try:
                    page2.goto(url, wait_until="domcontentloaded", timeout=timeout)
                except PWTimeoutError:
                    pass
                sleep(random.uniform(3.2, 8.1))
                content = page2.content()
                final_url = page2.url
                try:
                    ctx2.close()
                except Exception:
                    pass
            finally:
                headful_browser.close()
    finally:
        try:
            context.close()
        except Exception:
            pass
    return content, final_url

# ---------- Batch processing ----------
def process_url_list(urls: List[str]):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    with sync_playwright() as p:
        # keep a single headless browser for efficiency
        headless_browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        try:
            for idx, url in enumerate(urls, start=1):
                try:
                    print(f"Processing ({idx}/{len(urls)}): {url}", file=sys.stderr, flush = True)
                    wait_random(0.5, 2.0)
                    html, final_url = fetch_rendered_html_polite_with_browser(p, headless_browser, url, headful_fallback=True)
                    if not html:
                        print(f"Warning: no HTML for {url}", file=sys.stderr)
                        results.append((url, None, None))
                        # continue to next URL rather than exiting
                        wait_random(2.0, 6.0)
                        continue

                    fields = extract_article_fields_from_html(html, base_url=final_url or url)
                    dt = fields.get("published_dt")
                    slug = slugify_path_from_url(url)
                    filename_stub = filename_from_date_and_slug(dt, slug)

                    html_path = ensure_unique_path(OUT_DIR / f"{filename_stub}.html")
                    text_path = ensure_unique_path(OUT_DIR / f"{filename_stub}.txt")

                    # save original rendered HTML
                    try:
                        html_path.write_text(html, encoding="utf-8")
                    except Exception as e:
                        print(f"---Failed to write HTML for {url}: {e}", file=sys.stderr)

                    header_lines = [url]
                    if fields.get("title"):
                        header_lines.append(fields["title"])
                    if fields.get("category"):
                        header_lines.append(fields["category"])
                    if fields.get("published_raw"):
                        header_lines.append(fields["published_raw"])
                    header = "\n".join(header_lines).strip()
                    body_text = fields.get("article_text") or ""
                    full_text = f"{header}\n\n{body_text}".strip()

                    try:
                        text_path.write_text(full_text, encoding="utf-8")
                    except Exception as e:
                        print(f"---Failed to write text for {url}: {e}", file=sys.stderr)

                    print(html_path.resolve())
                    print(text_path.resolve())
                    results.append((url, str(html_path), str(text_path)))
                except Exception as e:
                    print(f"---Error processing {url}: {e}", file=sys.stderr)
                finally:
                    # polite pause between requests
                    wait_random(3.1, 15.3)
        finally:
            try:
                headless_browser.close()
            except Exception:
                pass
    return results

# ---------- Example usage ----------
def main():
    
    with open("./weblinks/all_links.txt", "r") as f_in:
        full_url_list = [line.strip() for line in f_in.readlines()]
    #end 
    url_list = full_url_list[5300:5400]
    # breaking up into chunks since there is over 6,600 articles. Each group of 10 taking a couple minutes
    # pattern is first 10 (0:10) then next 10 (10:20) etc
    # DONE 1300:5400
    # (must repeat last number when do next one, since python 0:10 means 0-9). Higher indexes are older.
    
    
    # optionally: read URLs from a file or command-line arguments
    # if len(sys.argv) > 1: url_list = sys.argv[1:]
    process_url_list(url_list)

if __name__ == "__main__":
    main()