from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request

link = input('Enter the link to the video: ')
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(20)
try:
    driver.get('https://ssstik.io/ru')
    elem = driver.find_element(By.ID, 'main_page_text')
    elem.clear()
    elem.send_keys(link)
    elem.send_keys(Keys.RETURN)
    xpath = '/html/body/main/section[1]/div/div/div[3]/div/div/div/a[1]'
    link_video = elem.find_element(by=By.XPATH, value=xpath).get_attribute('href')
    urllib.request.urlretrieve(link_video, 'video.mp4')
finally:
    driver.close()
