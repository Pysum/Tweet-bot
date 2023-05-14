from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_USERNAME = "@pysumM"
TWITTER_PASSWORD = "Sumit1988@#"
chrome_driver = "chromedriver.exe"
servie = Service(chrome_driver)
driver = webdriver.Chrome(service=servie)

driver.get('https://twitter.com/i/flow/login')
time.sleep(2)
login = driver.find_element(By.XPATH,'//input[@autocomplete="username"]')
login.send_keys(TWITTER_USERNAME)
login.send_keys(Keys.TAB)
login.send_keys(Keys.ENTER)
time.sleep(2)
password = driver.find_element(By.NAME,'password')
password.send_keys(TWITTER_PASSWORD)
password.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.ENTER)
time.sleep(2)
tweet = driver.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")
tweet.send_keys('How are you all?')
tweet.button= driver.find_element(By.XPATH,'//div[@data-testid="tweetButtonInline"]').click()
time.sleep(10)
driver.quit()