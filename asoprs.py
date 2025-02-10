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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.asoprs.org/member-directory-#/')
time.sleep(3)

driver.execute_script("""
      const shadowRoot = document.querySelector('sl-button[type="submit"]').shadowRoot.querySelector('button')
      shadowRoot.click()
    """)
time.sleep(5)

filtered_list=[]
while True:
    original_window=driver.current_window_handle
    cards=driver.find_elements(By.XPATH,'//div[@class="card__avatar"]/img')
    imglinks=[]
    for card in cards:
    
        imglinks.append(card.get_attribute('src'))

    print(imglinks)
    list_id=[]
    for link in imglinks:
        part=link.split('/')
        id=part[-2]
        list_id.append(id)
    print(list_id)
    for id in list_id:
        url=f"https://www.asoprs.org/index.php?option=com_community&view=profile&userid={id}#/profile"
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url)
        time.sleep(6)
        memberAdd=driver.find_elements(By.XPATH,'//div[contains(@class, "attribute-label")]/following-sibling::div[1]')
        try:
            member=memberAdd[0].text.strip()
            add=memberAdd[1].text
        except Exception:
            member='na'
            add='na'
        try:
            name=driver.find_element(By.XPATH,"//div[contains(@class, 'attribute-label') and contains(., 'Full Name')]/following-sibling::span").text
        except Exception:
            name='na'
        try:
            organization=driver.find_element(By.XPATH,"//div[contains(@class, 'attribute-label') and contains(., 'Organization')]/following-sibling::span").text
        except Exception:
            organization='na'

        filtered_list.append({
            'member':member,
            'address':add,
            'name':name,
            'organization':organization
        })
        time.sleep(2)
        print(filtered_list)
        driver.close()
        driver.switch_to.window(original_window)
    driver.execute_script("window.scroll(0,document.body.scrollHeight)")
    time.sleep(15)
    try:
        driver.execute_script("""
        const nextbutton = document.querySelector('button[class="mat-mdc-tooltip-trigger mat-mdc-paginator-navigation-next mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base"]')
        nextbutton.click()
        """)
    except Exception:
        print('all pages visited')
        break

#to csv  
df=pd.DataFrame(filtered_list)
os.makedirs('taskoutput',exist_ok=True)
path='taskoutput/info.csv'
df.to_csv(path,index=False)  
 


