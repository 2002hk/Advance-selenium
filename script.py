import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
### when subprocess set to False we have to execute inside if __name__=="__main__":
'''
if __name__ == '__main__':
    driver = uc.Chrome(headless=False, use_subprocess=False)
    driver.get('https://www.amazon.in/s?k=pendrive&page=1')
    print(driver.title)
    driver.quit()
'''
### when subprocess is set to True can write directly without the if block
driver = uc.Chrome(headless=False, use_subprocess=True)
driver.get('https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=728858856234&hvpos=&hvnetw=g&hvrand=15113598095295663664&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9145646&hvtargid=kwd-64107830&hydadcr=14452_2409549&gad_source=1')
print(driver.title)
search_box=driver.find_element("xpath",'//input[@id="twotabsearchtextbox"]')
search_box.send_keys('pendrive')
search_box.send_keys(Keys.ENTER)
time.sleep(3)
products=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 s-link-style a-text-normal"]')
original_window=driver.current_window_handle
filtered_data=[]
for product in products:
    get_link=product.get_attribute('href')
    product.click()
    for window_handle in driver.window_handles:
        if window_handle!=original_window:
            driver.switch_to.window(window_handle)
            break
    name=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]').text.strip()
    price=driver.find_element(By.XPATH,'//span[@class="a-price-whole"]').text.strip()
    brand=driver.find_element(By.XPATH,'//span[@class="a-size-base po-break-word"]').text.strip()
    filtered_data.append({
        'name':name,
        'price':price,
        'brand':brand
    })
    time.sleep(2)
    driver.close()
    driver.switch_to.window(original_window)
    

#to csv
df=pd.DataFrame(filtered_data)
os.makedirs('output2',exist_ok=True)
path='output2/pendrives.csv'
df.to_csv(path,index=False)