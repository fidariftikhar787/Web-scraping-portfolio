import requests
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import re

def url_to_filename(url):
    name = url.strip("/").split("/")[-1]
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    return f"{name}.html"



url = "https://www.zillow.com/professionals/real-estate-agent-reviews/chicago-il/"
Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "DNT": "1",  # Do Not Track
    "Upgrade-Insecure-Requests": "1"
}

cookies = [
    {
        "name": "_clck",
        "value": "17jxny4%7C2%7Cfx9%7C0%7C2009",
        "domain": ".zillow.com",
        "path": "/",
        "secure": False,
        "httpOnly": False,
        "expires": 1782974421  # use `expires` instead of `expirationDate`
    },
    {
        "name": "_clsk",
        "value": "u7ahik%7C1751447180433%7C5%7C0%7Ch.clarity.ms%2Fcollect",
        "domain": ".zillow.com",
        "path": "/",
        "secure": False,
        "httpOnly": False,
        "expires": 1751533580
    },
    {
        "name": "_fbp",
        "value": "fb.1.1751438421243.574548147951305353",
        "domain": ".zillow.com",
        "path": "/",
        "secure": False,
        "httpOnly": False,
        "expires": 1759223124
    },
    {
        "name": "_ga",
        "value": "GA1.2.794217745.1751438398",
        "domain": ".zillow.com",
        "path": "/",
        "secure": False,
        "httpOnly": False,
        "expires": 1786007179
    },
    {
        "name": "_gcl_au",
        "value": "1.1.340414741.1751438420",
        "domain": ".zillow.com",
        "path": "/",
        "secure": False,
        "httpOnly": False,
        "expires": 1759214420
    },

]

links =[]



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # browser = p.chromium.launch_persistent_context(
    #     user_data_dir="user-data-zillow",
    #     headless=False
    # )
    # page = browser.new_page()
    context = browser.new_context()
    # context.add_cookies(cookies)
    page = context.new_page()
    page.set_extra_http_headers({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/"
    })
    page.goto(url,timeout=90000, wait_until="domcontentloaded")
    page.mouse.move(300, 300)
    page.wait_for_timeout(2000)
    page.mouse.down()
    page.wait_for_timeout(1000)
    page.mouse.up()
    page.wait_for_load_state("load", timeout=90000)
    page.wait_for_selector("div.Grid-c11n-8-109-3__sc-18zzowe-0.gnIIpz",timeout=90000)
    # page.screenshot(path="blocked.png", full_page=True)
    html = page.inner_html("body")

    soup = HTMLParser(html)

    profiles = soup.css("div.Grid-c11n-8-109-3__sc-18zzowe-0.gnIIpz > a")

    profile_data = []


    for profile in profiles:
        link = profile.attrs["href"]
        links.append(link)
        print(link)
        # print(f"visiting {link}")

    Html = {}
    for link in links:


        # page = browser.new_page()
        context = browser.new_context()
        context.add_cookies(cookies)
        page = context.new_page()
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/"
        })
        try:
            page.goto(link, timeout=90000, wait_until="domcontentloaded")
            page.mouse.move(300, 300)
            page.wait_for_timeout(2000)
            page.mouse.down()
            page.wait_for_timeout(1000)
            page.mouse.up()
            page.wait_for_load_state("load", timeout=90000)
            page.wait_for_selector("div.ProfileFooter__ColoredDiv-sc-vpjfmb-0.cfBywH", timeout=90000)
            html = page.content()
            filename = url_to_filename(link)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Saved to: {filename}")
        except:
            print("failed to load url")
    browser.close()
        # resp2 = page.inner_html("body")
        # Data = HTMLParser(resp2)
        # Details = Data.css("div.ProfileFooter__ColoredDiv-sc-vpjfmb-0.cfBywH")[0]
        # Title = Details.css("div.Flex-c11n-8-107-0__sc-n94bjd-0.fCXUbl > img")[0].attrs["src"]
        # Name = Details.css("h1.Text-c11n-8-107-0__sc-aiai24-0.StyledHeading-c11n-8-107-0__sc-s7fcif-0.cJyrZF")[0].text()
        # containers = Details.css("div.Flex-c11n-8-107-0__sc-n94bjd-0.bXVNIZ")
        # Sales = Details.css("div[class='Flex-c11n-8-107-0__sc-n94bjd-0 eHkBjA'] div:nth-child(1) span:nth-child(1) strong:nth-child(1)").text()
        # Sales = containers[0].css("span.Text-c11n-8-107-0__sc-aiai24-0.gOSOFV")[0].text()
        # Total_Sales = containers[1].css("span.Text-c11n-8-107-0__sc-aiai24-0.gOSOFV")[0].text()
        # Price_Range = containers[2].css("span.Text-c11n-8-107-0__sc-aiai24-0.gOSOFV")[0].text()
        # Avg_Price = containers[3].css("span.Text-c11n-8-107-0__sc-aiai24-0.gOSOFV")[0].text()
        # Experience = containers[4].css("span.Text-c11n-8-107-0__sc-aiai24-0.gOSOFV")[0].text()
        # contact_info = Details.css("div.Flex-c11n-8-107-0__sc-n94bjd-0.ttNyW div.Flex-c11n-8-107-0__sc-n94bjd-0.ContactColumn__TextButtonFlexWrapper-sc-1ccc42g-0.fWizpG.bttiaK")
        # Phone = contact_info[0].css("a.StyledTextButton-c11n-8-107-0__sc-1nwmfqo-0.ezHcPX > span")[0].text()
        # Fax = contact_info[1].css("a.StyledTextButton-c11n-8-107-0__sc-1nwmfqo-0.ezHcPX > span")[0].text()
        # Email = contact_info[2].css("a.StyledTextButton-c11n-8-107-0__sc-1nwmfqo-0.ezHcPX > span")[0].text()
        # Address = contact_info[3].css("a.StyledTextButton-c11n-8-107-0__sc-1nwmfqo-0.ezHcPX > span")[0].text()
        #
        # print(Title)
        # print(Name)
        # print(Sales)
        # print(Total_Sales)
        # print(Price_Range)
        # print(Avg_Price)
        # print(Experience)
        # print(contact_info)
        # print(Phone)
        # print(Fax)
        # print(Email)
        # print(Address)




















