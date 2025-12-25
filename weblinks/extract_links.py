# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 23:14:09 2025

@author: jshilts
"""
#!/usr/bin/env python3
"""
extract_links_cf.py
Usage:
    python extract_links_cf.py <start_url> [output_file]

Tries to avoid Cloudflare bot pages and returns all anchor hrefs (one per line).
"""
import sys
import random
from pathlib import Path
from time import sleep
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeoutError

DEFAULT_OUTPUT = "links.txt"
DEFAULT_FILTER = "www.science.org/content/blog-post/"

COMMON_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
             "AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/120.0.0.0 Safari/537.36")

def usage():
    print("Usage: python extract_links_cf.py <start_url> [output_file]")
    sys.exit(2)

def extract_article_links(page, filter_substring):
    # Ask the page for absolute hrefs (element.href returns absolute URL)
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

def extract_all_article_links(page, filter_substring=None):
    # Ask the page for absolute hrefs (element.href returns absolute URL)
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
    # common phrases Cloudflare uses for JS checks
    if "checking your browser" in c or "just a moment" in c or "please enable javascript" in c:
        return True
    return False

def run_try(start_url, out_path, filter_substring=None):
    """Try headless first, then headful fallback if Cloudflare detected."""
    with sync_playwright() as p:
        # first attempt: headless with small anti-detection tweaks
        browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(user_agent=COMMON_UA, locale="en-US")
        # hide webdriver
        context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        # some sites check accept-language and referer-like headers
        context.set_extra_http_headers({"accept-language": "en-US,en;q=0.9", "referer": start_url})
        page = context.new_page()
        try:
            page.goto(start_url, wait_until="domcontentloaded", timeout=60000)
        except PWTimeoutError:
            # continue; page may still be usable
            pass

        content = page.content()
        url_after = page.url
        if looks_like_cloudflare(content, url_after):
            # headless likely blocked -> try headful fallback
            browser.close()
            # second attempt: headful (visible) so browser can fully run challenge
            browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
            context = browser.new_context(user_agent=COMMON_UA, locale="en-US")
            context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
            context.set_extra_http_headers({"accept-language": "en-US,en;q=0.9", "referer": start_url})
            page = context.new_page()
            try:
                page.goto(start_url, wait_until="domcontentloaded", timeout=60000)
            except PWTimeoutError:
                pass
            # Give the headful browser a short grace period to run challenge JS.
            # This does not "wait for me" — it gives the page JS time to complete.
            sleep(random.uniform(3, 10))
            content = page.content()
            url_after = page.url
            if looks_like_cloudflare(content, url_after):
                # Still got Cloudflare. We'll extract whatever links are present (likely the challenge page).
                print("Warning: page still looks like a Cloudflare challenge. Extracting whatever links are present.",
                      file=sys.stderr)

        # Extract links (all anchors) from whatever page we have
        links = extract_article_links(page, filter_substring)
        if not links:
            print("No filtered links found, returning all links.", file=sys.stderr)
            links = extract_all_article_links(page)

        browser.close()
    # save
    Path(out_path).write_text("\n".join(links) + ("\n" if links else ""), encoding="utf-8")
    return links

def main(argv):
    sleep(random.uniform(14, 132))
    if len(argv) < 2:
        usage()
    start_url = argv[1]
    out_file = argv[2] if len(argv) >= 3 else DEFAULT_OUTPUT
    filter_substring = argv[3] if len(argv) >= 4 else DEFAULT_FILTER
    try:
        links = run_try(start_url, out_file, filter_substring)
    except Exception as e:
        print("Error running Playwright:", e, file=sys.stderr)
        return 1
    print(f"Saved {len(links)} links to {Path(out_file).resolve()}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
