#!/usr/bin/env python3
"""
Update all RSVP HTML pages with the correct Google Apps Script URL.
Run this after deploying your Apps Script web app.
"""

import os
import glob

# ============================================================
# UPDATE THIS with your actual deployed Apps Script URL
# ============================================================
NEW_APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyWWdkWKaDCPQko62EpNtKb2SvXoB2g5o-8lNdE9viH-ylaB-Qs0FyvvpOhg2IesscW/exec"
# ============================================================

RSVP_DIR = "."

def main():
    html_files = glob.glob(os.path.join(RSVP_DIR, "party-*.html"))
    
    if not html_files:
        print(f"❌ No party HTML files found in '{RSVP_DIR}/'")
        print("   Run generate_pages.py first.")
        return
    
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "YOUR_APPS_SCRIPT_URL_HERE" in content:
            content = content.replace("YOUR_APPS_SCRIPT_URL_HERE", NEW_APPS_SCRIPT_URL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
    
    print(f"✅ Updated {count} HTML files with Apps Script URL")
    print(f"   URL: {NEW_APPS_SCRIPT_URL}")

if __name__ == '__main__':
    main()
