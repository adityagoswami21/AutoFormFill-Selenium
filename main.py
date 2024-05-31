from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://stackoverflow.com/questions/60117232/selenium-google-login-block#:~:text=The%20core%20problem%20here%20you,with%20your%20real%20account%20name.")
log_in = driver.find_element(By.XPATH, value="/html/body/header/div/nav/ol/li[3]/a").click()
cookies = driver.find_element(By.XPATH, value="//*[@id='onetrust-reject-all-handler']").click()
