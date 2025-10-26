from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")  
chrome_options.add_argument("--disable-notifications")  

navigateur = webdriver.Chrome(options=chrome_options)
navigateur.get("https://www.saucedemo.com/")
chercher_champs_1 = navigateur.find_element(By.ID,"user-name")
chercher_champs_1.clear()
chercher_champs_1.send_keys("standard_user")

chercher_champs_2 = navigateur.find_element(By.ID,"password")
chercher_champs_2.clear()
chercher_champs_2.send_keys("secret_sauce")

navigateur.find_element(By.ID,"login-button").click()
