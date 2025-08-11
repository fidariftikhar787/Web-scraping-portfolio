import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract(pageno):
    Agent_links = []
    # Start browser
    # options = uc.ChromeOptions()
    # options.headless = True
    driver = uc.Chrome()
    driver.get(f"https://www.zillow.com/professionals/real-estate-agent-reviews/chicago-il/?page={pageno}")

    try:
        container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[class="Grid-c11n-8-109-3__sc-18zzowe-0 gnIIpz"]')
            )
        )

        links = container.find_elements(By.TAG_NAME,"a")
        for link in links:
            href = link.get_attribute("href")
            if href != 'https://www.zillow.com/ods/submit_lead?request_type=ActFastV2&utm_campaign=agent_finder_cta&zipcode=60629':
                print(href)
                Agent_links.append(href)

        with open("Agents.txt", "a", encoding="utf-8") as f:
            for url in Agent_links:
                f.write(url + "\n")


    finally:
        driver.quit()

for i in range(1,4):
    extract(i)

