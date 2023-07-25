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
# cookies = WebDriverWait(scraper, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'acceptCookies')).click())
wait = WebDriverWait(scraper,10)
cookies_wait = scraper.find_element(By.CLASS_NAME, "acceptCookies")
wait.until(EC.element_to_be_clickable(cookies_wait))
cookies_wait.click()
data= []
unique_id = 0
while True:
    itemCards = scraper.find_elements(By.CLASS_NAME, "thumbnail")
    
    for items in itemCards:
        name = WebDriverWait(scraper, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )
        fname = items.find_element(By.CLASS_NAME, "title").get_attribute("title")
        price =  WebDriverWait(scraper, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pull-right.price"))
        )
        fprice = items.find_element(By.CLASS_NAME, "pull-right.price").text

        specifications =  WebDriverWait(scraper, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "description"))
        )
        fspecifications = items.find_element(By.CLASS_NAME, "description").text
        number_of_reviews = WebDriverWait(scraper, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ratings"))
        )
        fnumber_of_reviews = items.find_element(By.CLASS_NAME, "ratings").text
        unique_id += 1
        writer.writerow(
           [unique_id, fname, fprice, fspecifications, fnumber_of_reviews])
        # data.append([unique_id, name, price, specifications, number_of_reviews])
    try:
        scraper.find_element(By.LINK_TEXT, "›").click()
            
        
    except NoSuchElementException:
        break
    
  
    scraper.quit
    file.close
    


