from selenium import webdriver
import os
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform?pli=1")
time.sleep(1)

# name = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
# name.send_keys(os.getenv("NAME"))

# number = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
# number.send_keys(os.getenv("NUMBER"))

# email = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
# email.send_keys(os.getenv("EMAIL"))

# address = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea")
# address.send_keys(os.getenv("ADDRESS"))

# pincode = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
# pincode.send_keys(os.getenv("PINCODE"))

# dobdate = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input")
# dobdate.send_keys(os.getenv("DOBDATE"))
# dobmonth = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input")
# dobmonth.send_keys(os.getenv("DOBMONTH"))
# dobyear = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input")
# dobyear.send_keys(os.getenv("DOBYEAR"))
fields = [
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input", "NAME"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input", "NUMBER"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input", "EMAIL"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea", "ADDRESS"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input", "PINCODE"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input", "DOBDATE"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input", "DOBMONTH"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input", "DOBYEAR"),
    ("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input", "GENDER")
]
