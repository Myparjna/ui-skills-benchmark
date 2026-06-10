import os
from playwright.sync_api import sync_playwright

BASE_DIR = r"C:\Users\mypra\Desktop\前端设计skills大横评"
OUTPUT_DIR = os.path.join(BASE_DIR, "showcase", "assets", "screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# All 39 HTML files are in the kimi/ directory
folder = "kimi"
folder_path = os.path.join(BASE_DIR, folder)
files = sorted([f for f in os.listdir(folder_path) if f.endswith(".html")])

print(f"Found {len(files)} HTML files to screenshot")

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    for filename in files:
        filepath = os.path.join(folder_path, filename)
        output_path = os.path.join(OUTPUT_DIR, filename.replace(".html", ".png"))
        
        # Determine viewport
        if "charging" in filename:
            viewport = {"width": 390, "height": 844}
            # For charging pages, set a standard mobile viewport
        else:
            viewport = {"width": 1440, "height": 900}
        
        context = browser.new_context(viewport=viewport)
        page = context.new_page()
        page.goto(f"file:///{filepath}")
        page.wait_for_timeout(2500)  # Wait for animations/fonts/icons/charts
        page.screenshot(path=output_path, full_page=False)
        context.close()
        print(f"Screenshot: {filename} -> {output_path}")
    
    browser.close()

print("All screenshots done!")
