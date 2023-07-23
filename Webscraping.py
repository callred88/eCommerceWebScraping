from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv


file = open("laptops.csv", "w")
writer = csv.writer(file)
writer.writerow(["id", "name", "price", "specifications", "number of reviews"])

browser_driver = Service("C:\Users\Callr\Downloads\chromedriver_win32")
scraper = webdriver.Chrome(service=browser_driver)

scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
