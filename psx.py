import time
import pandas as pd
import requests
import urllib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chromedriver = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.psx.com.pk/psx/resources-and-tools/listings/listed-companies")
driver.maximize_window()
wait = WebDriverWait(driver, 30)

# numoflines = [12,10,8,24,28,6,20,20,6,7,25,11,30,35,2,8,6,24,30,4,10,10,13,17,1,4,29,10,14,56,63,10,3,7,4,1]
# df = pd.read_excel("data.xlsx", index_col=0)
# addition = 0
# index = 1 #to loop over list
# sector = Select(driver.find_element_by_id("sector"))

# for sec in sector.options[1:]:

# #     if sec.text == "Bonds" or sec.text == "Stock index future contracts" or sec.text == "Future contracts":
# #         continue 
    
#     print("Index {}, Company Name {} ".format(index, sec.text))
#     index += 1

chromedriver = "chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.psx.com.pk/psx/resources-and-tools/listings/listed-companies")
driver.maximize_window()
wait = WebDriverWait(driver, 30)

# numoflines = [56,63,10,3,7,4,1]
numoflines = [12,10,8,24,28,6,20,20,6,7,25,11,30,35,2,8,6,24,30,4,10,10,13,17,1,4,29,10,15,56,63,10,3,7,4,1]

df = pd.read_excel("data.xlsx", index_col=0)
# addition = 425+15
addition = 0
index = 0 #to loop over list
sector = Select(driver.find_element_by_id("sector"))

with open("textilecomposite.txt", "w") as myfile:
    for sec in sector.options[1:]:
                  
        if sec.text == "Bonds" or sec.text == "Stock index future contracts" or sec.text == "Future contracts":
            continue        
    
        sec.click()
        loop = numoflines[index]

        for i in range(loop):
            symbol = df['Ticker'][addition+i] 
            symbol = str(symbol).split()[0] #picks up symbol
            print(symbol)
            
            findelement = wait.until(EC.presence_of_element_located((By.ID, symbol)))
            findelement.click()

            # we do this after thingy has been clicked upon
            extract = wait.until(EC.presence_of_element_located((By.ID, "addressbookdata")))

            #close the popup
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close'][@data-dismiss='modal']"))).click()

            driver.execute_script("window.scrollBy(0,45);") #scroll down

            myfile.write(extract.get_attribute('innerText'))

        addition += loop
        index += 1
        driver.execute_script("window.scrollTo(0,0)")