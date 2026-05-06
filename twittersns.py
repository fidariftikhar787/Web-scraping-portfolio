# import ssl
# import certifi
# import snscrape.modules.twitter as sntwitter
# import urllib3
# urllib3.disable_warnings()
#
# # Force use of certifi bundle or bypass SSL entirely
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # Scrape tweets
# for i, tweet in enumerate(sntwitter.TwitterSearchScraper("python").get_items()):
#     print(f"{i+1}: {tweet.content}")
#     if i > 4:
#         break
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys





web = "https://x.com/"
driver = uc.Chrome(version_main=138)
driver.get(web)
driver.maximize_window()


login_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/login"]'))  # ← more stable than class
    )

# login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
login_input.click()
time.sleep(3)

username_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]'))  # ← more stable than class
    )

username = driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')
username.send_keys("@Ant3673Carboni")
time.sleep(3)


next = driver.find_element(By.CSS_SELECTOR, 'div[class="css-146c3p1 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci"] > span > span')
next.click()
time.sleep(3)

password_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]'))  # ← more stable than class
    )

password = driver.find_element(By.CSS_SELECTOR, 'input[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')
password.send_keys("Tpin@6907")
time.sleep(3)

sigin_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="css-146c3p1 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci"] > span > span'))  # ← more stable than class
    )

signin = driver.find_element(By.CSS_SELECTOR,'div[class="css-146c3p1 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci"] > span > span')
signin.click()
#
# input("✅ Signed in successfully. Press Enter to close...")

# article[role="article"]

# website = "https://x.com/search?q=f1&src=typed_query"
# driver = uc.Chrome()
# driver.get(website)
# driver.maximize_window()
# time.sleep(5)



search_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]'))  # ← more stable than class
    )

search = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]')
search.click()
search.send_keys("f1")
search.send_keys(Keys.ENTER)
time.sleep(3)


tweet_check = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'article[role="article"]'))  # ← more stable than class
    )

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        last_height = new_height

tweets = driver.find_elements(By.CSS_SELECTOR, 'article[role="article"]')

# div[data-testid="User-Name"] a span span
# div[data-testid="User-Name"] > div:nth-child(2) a span
# div[data-testid="tweetText"] > span
# div[data-testid="tweetPhoto"] > img

useraccounts = []
usernames = []
tweettexts = []
tweetphotos = []


for tweet in tweets:
    useraccount = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="User-Name"] a span span').text
    username = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="User-Name"] > div:nth-child(2) a span').text
    line = 'None'
    try:
        Texts = tweet.find_elements(By.CSS_SELECTOR, 'div[data-testid="tweetText"] > span')
        if len(Texts) > 1:
            line = ' '
            for Text in Texts:
                line = line + Text.text
        else:
            line = Texts[0].text
    except:
        continue
    photo = 'None'
    try:
        photo = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetPhoto"] > img').get_attribute("src")
    except:
        continue

    useraccounts.append(useraccount)
    usernames.append(username)
    tweettexts.append(line)
    tweetphotos.append(photo)

input("press enter to continue")
driver.quit()
df_tweets = pd.DataFrame({'useraccount': useraccounts, 'username' : usernames, 'Text':tweettexts, 'Photos':tweetphotos})
df_tweets.to_csv('tweets.csv',index=False)
print(df_tweets)


# with open("file.txt", 'a', encoding="utf-8") as f:
#     f.write(url + '\n')

import csv
with open("file.csv", 'a', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([])




















