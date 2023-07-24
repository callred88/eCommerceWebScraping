from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv


file = open("laptops.csv", "w")
writer = csv.writer(file)
writer.writerow(["id", "name", "price", "specifications", "number of reviews"])

browser_driver = Service("Users\Callr\Downloads\chromedriver_win32")
scraper = webdriver.Chrome(service=browser_driver)

#Here we grab the site and first page. 
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

data= []

itemCards = scraper.find_elements(By.CLASS_NAME, "thumbnail")
for item in itemCards:
    name = item.find_element(By.CLASS_NAME, "title").get_attribute("title")




