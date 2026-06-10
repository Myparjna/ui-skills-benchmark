import asyncio
import os
from playwright.async_api import async_playwright

EXHIBITION_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(EXHIBITION_DIR, 'assets', 'screenshots')
SERVER_URL = 'http://127.0.0.1:8766'

files = [
    'kimi-k2.6-design-taste-frontend-airline.html',
    'kimi-k2.6-design-taste-frontend-bikeops.html',
    'kimi-k2.6-design-taste-frontend-charging.html',
    'kimi-k2.6-frontend-design-airline.html',
    'kimi-k2.6-frontend-design-bikeops.html',
    'kimi-k2.6-frontend-design-charging.html',
    'kimi-k2.6-frontend-design-pro-airline.html',
    'kimi-k2.6-frontend-design-pro-bikeops.html',
    'kimi-k2.6-frontend-design-pro-charging.html',
    'kimi-k2.6-impeccable-airline.html',
    'kimi-k2.6-impeccable-bikeops.html',
    'kimi-k2.6-impeccable-charging.html',
    'kimi-k2.6-modern-frontend-design-airline.html',
    'kimi-k2.6-modern-frontend-design-bikeops.html',
    'kimi-k2.6-modern-frontend-design-charging.html',
    'kimi-k2.6-modern-web-design-airline.html',
    'kimi-k2.6-modern-web-design-bikeops.html',
    'kimi-k2.6-modern-web-design-charging.html',
    'kimi-k2.6-nuxt-ui-airline.html',
    'kimi-k2.6-nuxt-ui-bikeops.html',
    'kimi-k2.6-nuxt-ui-charging.html',
    'kimi-k2.6-shadcn-airline.html',
    'kimi-k2.6-shadcn-bikeops.html',
    'kimi-k2.6-shadcn-charging.html',
    'kimi-k2.6-sleek-design-mobile-apps-airline.html',
    'kimi-k2.6-sleek-design-mobile-apps-bikeops.html',
    'kimi-k2.6-sleek-design-mobile-apps-charging.html',
    'kimi-k2.6-stitch-design-airline.html',
    'kimi-k2.6-stitch-design-bikeops.html',
    'kimi-k2.6-stitch-design-charging.html',
    'kimi-k2.6-superdesign-airline.html',
    'kimi-k2.6-superdesign-bikeops.html',
    'kimi-k2.6-superdesign-charging.html',
    'kimi-k2.6-taste-skill-airline.html',
    'kimi-k2.6-taste-skill-bikeops.html',
    'kimi-k2.6-taste-skill-charging.html',
    'kimi-k2.6-ui-ux-pro-max-airline.html',
    'kimi-k2.6-ui-ux-pro-max-bikeops.html',
    'kimi-k2.6-ui-ux-pro-max-charging.html',
    'kimi-k2.6-web-design-guidelines-airline.html',
    'kimi-k2.6-web-design-guidelines-bikeops.html',
    'kimi-k2.6-web-design-guidelines-charging.html',
]

async def screenshot_page(browser, filename):
    is_mobile = 'charging' in filename
    url = f'{SERVER_URL}/pages/{filename}'
    out_path = os.path.join(SCREENSHOTS_DIR, filename.replace('.html', '.png'))

    context_kwargs = {}
    if is_mobile:
        context_kwargs = {
            'viewport': {'width': 414, 'height': 896},
            'device_scale_factor': 2
        }
    else:
        context_kwargs = {
            'viewport': {'width': 1920, 'height': 1080},
            'device_scale_factor': 1
        }

    context = await browser.new_context(**context_kwargs)
    page = await context.new_page()
    try:
        await page.goto(url, wait_until='networkidle', timeout=60000)
        await asyncio.sleep(2)
        await page.screenshot(path=out_path, full_page=False, type='png')
        print(f'OK: {filename}')
    except Exception as e:
        print(f'FAIL: {filename} - {e}')
    finally:
        await context.close()

async def main():
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for i, filename in enumerate(files):
            print(f'[{i+1}/{len(files)}] {filename}')
            await screenshot_page(browser, filename)
        await browser.close()
    print('All screenshots done!')

if __name__ == '__main__':
    asyncio.run(main())
