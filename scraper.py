from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
import json

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=728858856234&hvpos=&hvnetw=g&hvrand=15113598095295663664&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9145646&hvtargid=kwd-64107830&hydadcr=14452_2409549&gad_source=1')
time.sleep(10)

search_box=driver.find_element("xpath",'//input[@id="twotabsearchtextbox"]')
search_box.send_keys('pendrive')
search_box.send_keys(Keys.ENTER)
time.sleep(4)
pages=int(driver.find_element(By.XPATH,'//span[@class="s-pagination-item s-pagination-disabled"]').text.strip())
print(pages)
pages=2
count=0
filtered_data=[]
for i in range(1,pages+1):
    url=f'https://www.amazon.in/s?k=pendrive&page={i}'
    driver.get(url)
    driver.execute_script('window.scroll(0,document.body.scrollHeight)')

    products=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 s-link-style a-text-normal"]')
    links=[product.get_attribute('href') for product in products]


    #url='https://www.amazon.in/s?k=pendrive&page=1'
    
    
    for product in products:
        get_link=product.get_attribute('href')
        driver.execute_script("window.open('');") 
        driver.switch_to.window(driver.window_handles[1])
        driver.get(get_link)
        name=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]').text.strip()
        price=driver.find_element(By.XPATH,'//span[@class="a-price-whole"]').text.strip()
        brand=driver.find_element(By.XPATH,'//span[@class="a-size-base po-break-word"]').text.strip()
        filtered_data.append({
            'Name':name,
            'Price':price,
            'Brand':brand
        })
        count+=1
        print(count)
        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

print(filtered_data)

#to csv
dataframe=pd.DataFrame(filtered_data)
os.makedirs('output',exist_ok=True)
path='output/pendrives.csv'
dataframe.to_csv(path,index=False)

#to json
with open('C:/Users/hrutu/Desktop/advance selenium/output/pendrives.json','w') as f:
    json.dump(filtered_data,f)


    
    


    

#driver.quit()