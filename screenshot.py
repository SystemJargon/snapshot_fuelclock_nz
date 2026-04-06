import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import os

async def run():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Go to URL
        print("Navigating to FuelClock...")
        await page.goto("https://www.fuelclock.nz/", wait_until="networkidle")
        
        # Wait for dynamic content to load
        await asyncio.sleep(5) 
        
        # Create 'screenshots' folder if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
            
        # Save with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filepath = f"screenshots/fuel_{timestamp}.png"
        
        await page.screenshot(path=filepath, full_page=True)
        print(f"Screenshot saved: {filepath}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
