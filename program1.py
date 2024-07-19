from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/prajna/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.instagram.com/")
time.sleep(3)
username = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
username.send_keys("your username")
password = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys("your password")
password.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]""").click()
search=driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input""") 
search.send_keys("pora_nesiaparapio")
time.sleep(1)
driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]""").click()
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div/div[1]/div[1]/a""").click()
time.sleep(1)
driver.find_element_by_xpath("""/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button""").click()
driver.find_element_by_xpath("""/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button""").click()
time.sleep(2)

for i in range(2,11):
  
    driver.find_element_by_xpath("""/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button""").click()
    time.sleep(2)