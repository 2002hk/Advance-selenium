from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
# Initialize the WebDriver (make sure to specify the path to your WebDriver executable)
driver=uc.Chrome(headless=False,use_subprocess=True)
#driver = webdriver.Chrome()

# Navigate to the webpage containing the slider
driver.get('https://www.amazon.in/s?k=pendrive&page=1')

# Locate the slider element by its ID or any other selector
slider = driver.find_element(By.ID, "p_36/range-slider_slider-item_lower-bound-slider")

# Get the width of the slider
slider_width = slider.size['width']

print(f"Width of the slider: {slider_width} pixels")

# Close the browser
driver.quit()
