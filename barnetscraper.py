from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import json
import argparse
import os

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://publicaccess.barnet.gov.uk/online-applications/')
time.sleep(2)

tabs=driver.find_elements(By.XPATH,'//ul[@class="tabs"]/li/a')
tabs[1].click()

driver.find_element(By.XPATH,'//option[@value="FUL"]').click()

#set up argument parser
parser=argparse.ArgumentParser(description="Take date inputs for Selenium automation.")
parser.add_argument('--start_date',type=str,required=True)
parser.add_argument('--end_date',type=str,required=True)

#parse arguments
args=parser.parse_args()
start_date=args.start_date
end_date=args.end_date

start_date_field=driver.find_element(By.XPATH,"//input[@type='text' and @name='date(applicationReceivedStart)' and @id='applicationReceivedStart']")
end_date_field=driver.find_element(By.XPATH,"//input[@type='text' and @name='date(applicationReceivedEnd)' and @id='applicationReceivedEnd']")

start_date_field.send_keys(start_date)
end_date_field.send_keys(end_date)

driver.find_element(By.XPATH,'//input[@type="submit" and @value="Search"]').click()
filtered_data=[]


#next_page_url=driver.find_element(By.XPATH,'//a[@class="next"]').get_attribute('href')
try:
    next_page=driver.find_element(By.XPATH,'//span[@class="showing"]/text()').text
    no_of_pages=int(next_page.split()[-1])
    print(no_of_pages)
except Exception as e:
    no_of_pages=1

#next_page=driver.find_element(By.XPATH,'//a[@class="next"]')
while True:
    original_window=driver.current_window_handle

    #containers=driver.find_elements(By.XPATH,'//li[@class="searchresult"]')
    container_link=driver.find_elements(By.XPATH,'//ul[@id="searchresults"]//a[1]')
    links=[]
    for link in container_link:
        links.append(link.get_attribute('href'))
    print(links)

    for link in links:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        driver.get(link)

        #extracting element
        table=driver.find_elements(By.XPATH,'//table[@id="simpleDetailsTable"]//td')
        try:
            ref=table[0].text
        except Exception as e:
            ref='na'
        try:
            alt_red=table[1].text
        except Exception as e:
            alt_red='na'
        try:  
            app_recv=table[2].text
        except Exception as e:
            app_recv='na'

        try:
            app_val=table[3].text
        except Exception as e:
            app_val='na'
        try:
            add=table[4].text
        except Exception as e:
            add='na'
        try:
            proposal=table[5].text
        except Exception as e:
            proposal='na'
        try:
            status=table[6].text
        except Exception as e:
            status='na'

        filtered_data.append({
            'ref':ref,
            'alt_red':alt_red,
            'app_recv':app_recv,
            'app_val':app_val,
            'add':add,
            'proposal':proposal,
            'status':status
        })
       
        driver.close()
        driver.switch_to.window(original_window)
        
    #driver.switch_to.window(original_window)
    try:
        next_page=driver.find_element(By.XPATH,'//a[@class="next"]')
        next_page.click()
        time.sleep(2)
    except Exception:
        print('No more pages to scrape')
        break
    
print(filtered_data)
print(len(filtered_data))

#to csv
df=pd.DataFrame(filtered_data)
os.makedirs('ext_output2',exist_ok=True)
path='ext_output2/info.csv'
df.to_csv(path,index=False)

#to json
with open('C:/Users/hrutu/Desktop/advance selenium/ext_output2/info.json','w') as f:
    json.dump(filtered_data,f) 


    

    
    





