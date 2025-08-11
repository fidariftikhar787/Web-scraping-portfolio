import asyncio
from undetected_playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import csv


async def extract():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context()
        page = await context.new_page()

        url = "https://www.google.com/maps/search/interior+design/@24.9264171,67.0372785,13.52z?entry=ttu&g_ep=EgoyMDI1MDcwOS4wIKXMDSoASAFQAw%3D%3D"
        await page.goto(url,timeout=90000)
        await page.wait_for_load_state("load")

        # Wait for scrollable sidebar
        scroll_selector = 'div[role="feed"]'

        await page.wait_for_selector(scroll_selector)

        # Scroll multiple times to load more businesses
        for i in range(5):
            await page.evaluate(f'''
                () => {{
                    const scrollable = document.querySelector('{scroll_selector}');
                    if (scrollable) {{
                        scrollable.scrollBy(0, 2000);
                    }}
                }}
            ''')
            await page.wait_for_timeout(5000)

        # cards = await page.query_selector_all('.Nv2PK')
        # print(f"✅ Found {len(cards)} business cards")
        html = await page.content()
        await browser.close()

        soup = BeautifulSoup(html,'html.parser')

        listings = soup.find_all("div", class_='Nv2PK tH5CWc THOPZb')
        print(len(listings))

        for listing in listings:
            Name = listing.find("div",class_='qBF1Pd fontHeadlineSmall').get_text(strip=True)
            Rating = ''
            try:
                Rating = listing.find("span",class_='MW4etd').get_text(strip=True),
                Rating = Rating[0]
                NumberOfReviews = listing.find("span",class_='UY7F9').get_text(strip=True).strip('()')
            except:
                Rating = ''
                NumberOfReviews = 0
            Phone = listing.find("span",class_='UsdlK').get_text(strip=True)
            try:
                Adrress = listing.select_one('div.W4Efsd > div.W4Efsd:nth-of-type(1) > span > span:nth-of-type(2)').get_text(strip=True).strip("")

            except:
                Adrress=''

            with open("map_details.csv", "a", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [Name, Rating,NumberOfReviews,Phone,Adrress])
            # print(
            #     {
            #         'Name':Name,
            #         'Rating':Rating,
            #         'NumberOfReviews':NumberOfReviews,
            #         'Phone':Phone,
            #         'Address':Address
            #     }
            # )

asyncio.run(extract())






