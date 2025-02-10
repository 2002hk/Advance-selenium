from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
import pandas as pd
import json
import argparse 
import os

driver = uc.Chrome(headless=False, use_subprocess=True)
#driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.imdb.com/list/ls528979552/')
time.sleep(4)
driver.execute_script('window.scroll(0,document.body.scrollHeight)')


movie_container=driver.find_elements(By.XPATH,'//div[@class="ipc-metadata-list-summary-item__tc"]')
print(len(movie_container))
time.sleep(8)
filtered_list=[]
for movie in movie_container:
    try:
        name=driver.find_element(By.XPATH,'.//h3').text
    except Exception:
        name='na'
    try:
        year=driver.find_element(By.XPATH,'//div[@class="sc-d5ea4b9d-6 hBxwRe dli-title-metadata"]/span[1]').text
    except Exception:
        year='na'
    try:
        duration=driver.find_element(By.XPATH,'.//div[@class="sc-d5ea4b9d-6 hBxwRe dli-title-metadata"]/span[2]').text
    except Exception:
        duration='na'
    try:
        rating=driver.find_element(By.XPATH,'.//div[@class="sc-d5ea4b9d-6 hBxwRe dli-title-metadata"]/span[3]').text
    except Exception:
        rating='na'
    try:
        star=driver.find_element(By.XPATH,'.//span[@class="ipc-rating-star--rating"]').text
    except Exception:
        star='na'
    try:
        metascore=driver.find_element(By.XPATH,'.//span[@class="sc-b0901df4-0 bXIOoL metacritic-score-box"]').text
    except Exception:
        metascore='na'
    try:
        plot=driver.find_element(By.XPATH,'.//div[@class="ipc-html-content ipc-html-content--base sc-d49a611d-0 gKxuCN sttd-plot-container"]/div').text
    except:
        plot='na'
    try:
        cast=driver.find_elements(By.XPATH,'.//div[@class="ipc-html-content ipc-html-content--base sc-d49a611d-0 gKxuCN sttd-plot-container"]/div')
        actors=[element.text for element in cast]
    except Exception:
        actors='na'
    filtered_list.append({
        'Name':name,
        'Year':year,
        'Duration':duration,
        'Rating':rating,
        'Star':star,
        'MetaScore':metascore,
        'Plot':plot,
        'Cast':actors
    })
    print(filtered_list)
    print('*********The length of list',len(filtered_list))

print('**********************Length***************',len(filtered_list))

df=pd.DataFrame(filtered_list)
path='output/movies.csv'
df.to_csv(path,index=False)

with open('C:/Users/hrutu/Desktop/advance selenium/output/movies.json','w') as f:
    json.dump(filtered_list,f)



