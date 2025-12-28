# -*- coding: utf-8 -*-
# Creates index.json directory for the website to use
# run this on command line as 
# > python index-json-maker.py

import os
import re
import json
from datetime import datetime

RESP_DIR = "./responses"
OUT_PATH = os.path.join("./index.json")

MONTHS = {
    'january': '01','february': '02','march': '03','april': '04','may': '05','june': '06',
    'july': '07','august': '08','september': '09','october': '10','november': '11','december': '12'
}

def parse_date_from_filename(name):
    # Look for YYYYMMDD or YYYY-MM-DD or YYYY_MM_DD or YYYY.MM.DD
    m = re.search(r'(?P<y>\d{4})[^\d]?(?P<m>\d{2})[^\d]?(?P<d>\d{2})', name)
    if m:
        try:
            return f"{m.group('y')}-{m.group('m')}-{m.group('d')}"
        except Exception:
            pass
    return None

def parse_iso_in_text(text):
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)
    if m:
        y,mn,d = m.groups()
        try:
            datetime(int(y), int(mn), int(d))
            return f"{y}-{mn}-{d}"
        except Exception:
            return None
    return None

def parse_month_year_parenthetical_from_h1(text):
    # Find H1 header
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('#'):
            # match "Some Title (December 2014)" or "Title (Dec 2014)"
            m = re.search(r'\((?P<month>[A-Za-z]{3,9})\.?\s+(?P<year>\d{4})\)', line)
            if m:
                month = m.group('month').lower()
                year = m.group('year')
                month_num = MONTHS.get(month[:3] if len(month)>3 else month, MONTHS.get(month))
                if month_num:
                    # use day 01 as a fallback
                    return f"{year}-{month_num}-01"
    return None

def extract_title_from_h1(text):
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('#'):
            # remove initial '#' characters and surrounding whitespace
            title = re.sub(r'^#+\s*', '', line).strip()
            # remove trailing parenthetical like "(December 2014)" or "(2014-12-10)"
            title = re.sub(r'\s*\([^)]*\)\s*$', '', title).strip()
            return title
    return None

def extract_score(text):
    if not text:
        return None

    # Pattern 1: "Score: 7", "Score - 7", "Rating: 8", "Rating:9.5", case-insensitive
    # Handles optional spaces around : or -
    m = re.search(r'(Score|Rating)\s*[:\-]?\s*(\d+(?:\.\d+)?)', text, re.IGNORECASE)
    if m:
        try:
            value = m.group(2)
            return int(value) if '.' not in value else float(value)
        except ValueError:
            pass

    # Pattern 2: Bold full score like "**Score: 7**" or "**Rating: 8**"
    m2 = re.search(r'\*\*(Score|Rating):\s*(\d+(?:\.\d+)?)\*\*', text, re.IGNORECASE)
    if m2:
        try:
            value = m2.group(2)
            return int(value) if '.' not in value else float(value)
        except ValueError:
            pass

    # Pattern 3: Bold out-of format like "**8/10**", "**9.5/10**", "**7 / something**"
    m3 = re.search(r'\*\*\s*(\d+(?:\.\d+)?)\s*/', text)
    if m3:
        try:
            value = m3.group(1)
            return int(value) if '.' not in value else float(value)
        except ValueError:
            pass

    # Pattern 4: "Rating: 8/10" or "Rating:8/10" (with or without space)
    m4 = re.search(r'(Rating)\s*[:\-]?\s*(\d+(?:\.\d+)?)\s*/', text, re.IGNORECASE)
    if m4:
        try:
            value = m4.group(2)
            return int(value) if '.' not in value else float(value)
        except ValueError:
            pass

    # Pattern 5: **Score**: 7, **Score:** 7, **Score**:7, **Rating**: 8/10
    m1 = re.search(r'\*\*(Score|Rating)\s*:?\s*\*\*\s*(\d+(?:\.\d+)?)\s*(?:/.*)?', text, re.IGNORECASE)
    if m1:
        value = m1.group(2)
        return int(value) if '.' not in value else float(value)

    return None

def process_file(path, fname):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='latin-1') as f:
            text = f.read()

    # filename-based date
    date = parse_date_from_filename(fname) or parse_iso_in_text(text) or parse_month_year_parenthetical_from_h1(text)
    title = extract_title_from_h1(text) or os.path.splitext(fname)[0]
    score = extract_score(text)

    return {
        "filename": fname,
        "date": date,
        "title": title,
        "score": score
    }

def main():
    entries = []
    if not os.path.isdir(RESP_DIR):
        raise SystemExit(f"Directory not found: {RESP_DIR}")

    for fname in os.listdir(RESP_DIR):
        if not fname.lower().endswith('.md'):
            continue
        full = os.path.join(RESP_DIR, fname)
        if not os.path.isfile(full):
            continue
        entry = process_file(full, fname)
        entries.append(entry)

    # sort by date, descending if needed; if date is None, place at the end
    def date_key(e):
        if e['date']:
            return e['date']
        else:
            return '9999-12-31'  # push None dates to end

    entries = sorted(entries, key=date_key)

    # write index.json
    with open(OUT_PATH, 'w', encoding='utf-8') as out:
        json.dump(entries, out, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
