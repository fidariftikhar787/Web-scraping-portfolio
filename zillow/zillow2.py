import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Start browser
def extract(link):
    driver = uc.Chrome()
    driver.get(link)

    # try:
    #     # Wait for the phone number element to be present
    #     phone_elem = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located(
    #             (By.CSS_SELECTOR, 'div[class*="ContactColumn__TextButtonFlexWrapper"] > a')
    #         )
    #     )
    #
    #     # Extract and print phone number
    #     phone_number = phone_elem.text.strip()
    # except:
    #     driver.save_screenshot("headless_view.png")
    Name = ''
    try:
        Name_Elem = driver.find_element(By.CSS_SELECTOR,'h1[class="Text-c11n-8-107-0__sc-aiai24-0 StyledHeading-c11n-8-107-0__sc-s7fcif-0 cJyrZF"]')
        Name = Name_Elem.text.strip()
    except: Name=''

    Sales = Total_Sales = Price_Range = Avg_Price = Experience = ""

    try:
        FiveDivs = driver.find_elements(By.CSS_SELECTOR,'div[class="Flex-c11n-8-107-0__sc-n94bjd-0 bXVNIZ"]')
        if len(FiveDivs) == 5:
            try: Sales = FiveDivs[0].find_element(By.TAG_NAME, 'strong').text.strip()
            except: Sales = ''
            try:Total_Sales = FiveDivs[1].find_element(By.TAG_NAME, 'strong').text.strip()
            except:Total_Sales=''
            try:Price_Range = FiveDivs[2].find_element(By.TAG_NAME, 'strong').text.strip()
            except: Price_Range=''
            try:Avg_Price = FiveDivs[3].find_element(By.TAG_NAME, 'strong').text.strip()
            except:Avg_Price = ''
            try:Experience = FiveDivs[4].find_element(By.TAG_NAME, 'strong').text.strip()
            except: Experience=''
        else:
            try:Sales = FiveDivs[0].find_element(By.TAG_NAME, 'strong').text.strip()
            except:Sales=''
            try:Total_Sales = FiveDivs[1].find_element(By.TAG_NAME, 'strong').text.strip()
            except:Total_Sales=''
            try:Price_Range = FiveDivs[2].find_element(By.TAG_NAME, 'strong').text.strip()
            except:Price_Range=''
            try:Avg_Price = FiveDivs[3].find_element(By.TAG_NAME, 'strong').text.strip()
            except: Avg_Price=''
            Experience = ''
    except:
        print("not found")

    Phone = Fax = Email = Address = ""

    try:
        FourDivs = driver.find_elements(By.CSS_SELECTOR,'div[class="Flex-c11n-8-107-0__sc-n94bjd-0 ContactColumn__TextButtonFlexWrapper-sc-1ccc42g-0 fWizpG bttiaK"]')
        if len(FourDivs) == 4:
            try:Phone = FourDivs[0].find_element(By.TAG_NAME,'a').text.strip()
            except:Phone=''
            try:Fax = FourDivs[1].find_element(By.TAG_NAME,'a').text.strip()
            except:Fax=''
            try:Email = FourDivs[2].find_element(By.TAG_NAME,'a').text.strip()
            except:Email=''
            try:Address = FourDivs[3].find_element(By.TAG_NAME,'a').text.strip()
            except:Address=''
        else:
            try:Phone = FourDivs[0].find_element(By.TAG_NAME, 'a').text.strip()
            except:Phone=''
            Fax =''
            try:Email = FourDivs[1].find_element(By.TAG_NAME, 'a').text.strip()
            except:Email=''
            try:Address = FourDivs[2].find_element(By.TAG_NAME, 'a').text.strip()
            except:Address=''
    except:
        print("not found")


    # with open("Agent_details.txt", 'a', encoding="utf-8") as f:
    #     f.write(Name + ',' + Sales +','+Total_Sales+','+Price_Range+','+Avg_Price+','+Experience+','+Phone+','+Fax+','+Email+','+Address + "\n")

    with open("Agent_details.csv", "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([Name, Sales, Total_Sales, Price_Range, Avg_Price, Experience, Phone, Fax, Email, Address])

    driver.quit()

    # except Exception as e:
    #     print(f"Could not find phone number. Error: {e}")
    #
    # finally:
    #     driver.quit()

with open("Agents.txt", "r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]

for link in links[15:]:
    extract(link)
