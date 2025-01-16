import time
import undetected_chromedriver as uc
driver = uc.Chrome(headless=False,use_subprocess=True)
driver.get('https://nowsecure.nl')
time.sleep(4)
driver.save_screenshot('nowsecure.png')