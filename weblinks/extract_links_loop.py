# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 23:14:09 2025

@author: jshilts

MUST run on powershell / command prompt 
"""
#> cd "C:\Users\jshilts\OneDrive\Documents\Other Documents\Programming\Python\out-the-pipeline"
#>  .\.venv\Scripts\activate
#> python extract_links_loop.py

"""
extract_links_cf.py
Single-browser, multiple URL processing with per-context isolation.
"""
import sys
import random
from pathlib import Path
from time import sleep
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeoutError

DEFAULT_OUTPUT = "all_links.txt"
DEFAULT_FILTER = "www.science.org/content/blog-post/"

UA_LIST = [
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
     "AppleWebKit/537.36 (KHTML, like Gecko) "
     "Chrome/120.0.0.0 Safari/537.36"),
    ("Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) "
     "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"),
    ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
     "Chrome/120.0.0.0 Safari/537.36"),
]

def extract_article_links(page, filter_substring):
    hrefs = page.evaluate("""() =>
        Array.from(document.querySelectorAll('a'))
             .map(a => a.href)
             .filter(h => h)
    """)
    seen = set()
    results = []
    if filter_substring:
        for h in hrefs:
            if filter_substring in h and h not in seen:
                seen.add(h)
                results.append(h)
    else:
        for h in hrefs:
            if h not in seen:
                seen.add(h)
                results.append(h)
    return results

def extract_all_article_links(page):
    hrefs = page.evaluate("""() =>
        Array.from(document.querySelectorAll('a'))
             .map(a => a.href)
             .filter(h => h)
    """)
    seen = set()
    results = []
    for h in hrefs:
        if h not in seen:
            seen.add(h)
            results.append(h)
    return results

def looks_like_cloudflare(content, url):
    u = (url or "").lower()
    if "cloudflare.com" in u:
        return True
    if not content:
        return False
    c = content.lower()
    if "checking your browser" in c or "just a moment" in c or "please enable javascript" in c:
        return True
    return False

def wait_random(min_sec=2.0, max_sec=6.0):
    sleep(random.uniform(min_sec, max_sec))

def process_url_with_context(browser, p, url, filter_substring):
    ua = random.choice(UA_LIST)
    context = browser.new_context(user_agent=ua, locale="en-US")
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    context.set_extra_http_headers({"accept-language": "en-US,en;q=0.9", "referer": url})
    page = context.new_page()
    links = []
    try:
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
        except PWTimeoutError:
            pass
        content = page.content()
        url_after = page.url
        if looks_like_cloudflare(content, url_after):
            context.close()
            headful_browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
            try:
                ctx2 = headful_browser.new_context(user_agent=ua, locale="en-US")
                ctx2.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
                ctx2.set_extra_http_headers({"accept-language": "en-US,en;q=0.9", "referer": url})
                page2 = ctx2.new_page()
                try:
                    page2.goto(url, wait_until="domcontentloaded", timeout=60000)
                except PWTimeoutError:
                    pass
                sleep(random.uniform(3.2, 10.8))
                content = page2.content()
                url_after = page2.url
                if looks_like_cloudflare(content, url_after):
                    print(f"Warning: {url} still looks like a Cloudflare challenge.", file=sys.stderr)
                links = extract_article_links(page2, filter_substring)
                if not links:
                    links = extract_all_article_links(page2)
                ctx2.close()
            finally:
                headful_browser.close()
        else:
            links = extract_article_links(page, filter_substring)
            if not links:
                links = extract_all_article_links(page)
    except Exception as e:
        print(f"Error processing {url}: {e}", file=sys.stderr)
    finally:
        try:
            context.close()
        except Exception:
            pass
    return links

def run_try_many(urls, out_path, filter_substring=None):
    all_links = []
    seen_global = set()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        try:
            for idx, url in enumerate(urls, start=1):
                print(f"Processing ({idx}/{len(urls)}): {url}", file=sys.stderr)
                links = process_url_with_context(browser, p, url, filter_substring)
                for l in links:
                    if l not in seen_global:
                        seen_global.add(l)
                        all_links.append(l)
                wait_random(2.1, 8.4)
        finally:
            browser.close()
    Path(out_path).write_text("\n".join(all_links) + ("\n" if all_links else ""), encoding="utf-8")
    return all_links

def main():
    # Hardcode or define URLs here
    urls_to_test = [
        "https://www.science.org/blogs/pipeline?startPage=" + str(x) + "&pageSize=100" for x in range(0,68+1)
    ]
    out_file = DEFAULT_OUTPUT
    filter_substring = DEFAULT_FILTER

    links = run_try_many(urls_to_test, out_file, filter_substring)
    print(f"Saved {len(links)} links to {Path(out_file).resolve()}")

if __name__ == "__main__":
    main()
