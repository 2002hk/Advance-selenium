from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

with webdriver.Chrome() as driver:
    driver.get("https://www.amazon.in/s?k=pendrive&page=1")

    #setting up wait for later
    wait=WebDriverWait(driver,10)

    #storing the id of the original window
    original_window=driver.current_window_handle
    print(original_window)

    #to check we don't have another window open 
    assert len(driver.window_handles)==1

    #click the link which opens in a window
    products=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 s-link-style a-text-normal"]')
    links=[]
    for product in products:
        product.click()
    

    

    #wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    #loop through until we find a new window handle

    for window_handle in driver.window_handles:
        if window_handle!=original_window:
            driver.switch_to.window(window_handle)
            break

    #wait for the new tab to finsih loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))
