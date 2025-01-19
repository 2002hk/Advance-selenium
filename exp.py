import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
from selenium.webdriver.common.action_chains import ActionChains

driver=uc.Chrome(headless=False,use_subprocess=True)
driver.get('https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=728858856234&hvpos=&hvnetw=g&hvrand=15113598095295663664&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9145646&hvtargid=kwd-64107830&hydadcr=14452_2409549&gad_source=1')
print(driver.title)
search_box=driver.find_element("xpath",'//input[@id="twotabsearchtextbox"]')
search_box.send_keys('pendrive')
search_box.send_keys(Keys.ENTER)
time.sleep(2)
original_window=driver.current_window_handle
filters=driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-double-large"]//span[@class="a-declarative"]')
print(filters[1])
#filters[1].find_element(By.XPATH,'//div[@class="a-section a-spacing-double-large"]//span[@class="a-declarative"]//a').click()
time.sleep(3)
# Locate the slider element by its ID or any other selector
slider = driver.find_element(By.ID, "p_36/range-slider_slider-item_lower-bound-slider")
# Get the width of the slider
slider_width = slider.size['width']

#max_value=driver.find_element(By.XPATH,'//label[@class="a-form-label sf-range-slider-label sf-upper-bound-label"]/span/text()')
#min_value=driver.find_element(By.XPATH,'//label[@class="a-form-label sf-range-slider-label sf-lower-bound-label"]/span/text()')
desired_value=400
offset=(desired_value/100)*slider_width
actions=ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(offset, 0).release().perform() 
time.sleep(3)
button=driver.find_element(By.XPATH,'//input[@class="a-button-input"]').click()
time.sleep(10)
print('went to the next page')

driver.close()