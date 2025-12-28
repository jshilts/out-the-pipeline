# -*- coding: utf-8 -*-
"""
Sometimes the HTML extractor leaves in unwannted extra bits.
This cleans them and revises the prompt file in-place

Walks './prompts/' and for every '.txt' file:
  - removes the block starting at "Home (https://www.science.org/)" up through
    the last occurrence of any of the specified social-link tokens (if present)
  - removes "About the author Derek Lowe" and everything after it (if present)

Overwrites files in-place (UTF-8). 
"""
import os

PROMPTS_DIR = './'  # './prompts/'

# start and candidate end tokens (exact strings as requested)
START_TOKEN = 'Home (https://www.science.org/)'
END_TOKENS = [
    '(https://www.science.org/#email) Email',
    '(https://www.science.org/#whatsapp) Whatsapp',
    '(https://www.science.org/#wechat) Wechat',
    '(https://www.science.org/#reddit) Reddit',
    '(https://www.science.org/#linkedin) Linked',
    '(https://www.science.org/#facebook) Facebook',
]

AUTHOR_TOKEN = 'About the author Derek Lowe'

def process_text(text: str) -> str:
    # 1) Remove Home(...) block up through the last matching end token, if present.
    start_idx = text.find(START_TOKEN)
    if start_idx != -1:
        # find the last occurrence (global) of any END_TOKEN that occurs after start_idx
        last_end = -1
        for t in END_TOKENS:
            i = text.rfind(t)  # rfind global last occurrence
            if i != -1 and i + len(t) > last_end:
                last_end = i + len(t)
        # only remove if we found an end token that comes after the start token
        if last_end > start_idx:
            # remove the slice [start_idx:last_end]
            text = text[:start_idx] + text[last_end:]
            # collapse any repeated newlines that may have been created
            # (leave minimal single blank line)
            text = text.replace('\r\n', '\n').replace('\r', '\n')

    # 2) If "About the author Derek Lowe" is present, remove it and everything after.
    aidx = text.find(AUTHOR_TOKEN)
    if aidx != -1:
        text = text[:aidx]

    # Trim trailing whitespace but keep a single trailing newline
    text = text.rstrip() + '\n'
    return text

def main():
    changed_files = []
    if not os.path.isdir(PROMPTS_DIR):
        print(f"Directory not found: {PROMPTS_DIR}")
        return

    for entry in os.listdir(PROMPTS_DIR):
        if not entry.lower().endswith('.txt'):
            continue
        path = os.path.join(PROMPTS_DIR, entry)
        if not os.path.isfile(path):
            continue

        try:
            with open(path, 'r', encoding='utf-8') as fh:
                original = fh.read()
        except UnicodeDecodeError:
            # try with latin-1 as fallback
            with open(path, 'r', encoding='latin-1') as fh:
                original = fh.read()

        processed = process_text(original)

        if processed != original:
            # overwrite file with UTF-8
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(processed)
            changed_files.append(path)

    if changed_files:
        print("Processed and updated files:")
        for p in changed_files:
            print(" -", p)
    else:
        print("No changes made (no matching patterns found).")

if __name__ == '__main__':
    main()
