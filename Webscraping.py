from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


file = open("laptops.csv", "w")
writer = csv.writer(file)
writer.writerow(["id", "name", "price", "specifications", "number of reviews"])

browser_driver = Service("Users\Callr\Downloads\chromedriver_win32")
scraper = webdriver.Chrome(service=browser_driver)

#Here we grab the site and first page. 
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

#Waiting call to handle cookies popup. 
#cookies = WebDriverWait(scraper, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'acceptCookies')).click())
wait = WebDriverWait(scraper,10)
cookies_wait = scraper.find_element(By.CLASS_NAME, "acceptCookies")
wait.until(EC.element_to_be_clickable(cookies_wait))

data= []

itemCards = scraper.find_elements(By.CLASS_NAME, "thumbnail")
unique_id = 1
for items in itemCards:
    name = items.find_element(By.CLASS_NAME, "title")
    price = items.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[6]/div/div[1]/h4[1]")
    specifications = items.find_element(By.CLASS_NAME, "description")
    number_of_reviews = items.find_element(By.CLASS_NAME, "ratings")
    writer.writerow(
    [unique_id, name.text, price.text, specifications.text, number_of_reviews.text])
    unique_id += 1

    try:
        scraper.find_element(By.LINK_TEXT, "›").click()
        
    except NoSuchElementException:
        break


file.close
scraper.quit


