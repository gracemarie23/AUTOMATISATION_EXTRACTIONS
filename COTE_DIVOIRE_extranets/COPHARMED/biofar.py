from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

load_dotenv()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")  
chrome_options.add_argument("--disable-notifications")  
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.default_content_setting_values.notifications": 2,
    "profile.default_content_settings.popups": 0,

    "profile.password_manager_leak_detection": False,
    "profile.password_dismiss_compromised_alert": True,
}
chrome_options.add_experimental_option("prefs", prefs)

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")

navigateur = webdriver.Chrome(options=chrome_options)


navigateur.get("https://service02ab.eurapharma.com/cgiphl/pw_call.pgm?PGMA=VID020")

user_1 = os.getenv('user_biofar')
mdp_1  = os.getenv('mdp_biofar')
id_1 = os.getenv('id_1')

chercher_champs_1 = navigateur.find_element(By.NAME,"name1")
chercher_champs_1.clear()
chercher_champs_1.send_keys(user_1)

chercher_champs_2 = navigateur.find_element(By.NAME,"name2")
chercher_champs_2.clear()
chercher_champs_2.send_keys(mdp_1)

chercher_champs_2.send_keys(Keys.ENTER)

time.sleep(3)

WebDriverWait(navigateur, 10).until(
    EC.presence_of_element_located((By.ID, "f1_4"))
)

chercher_champs_id_1 = navigateur.find_element(By.ID,"f1_4")
chercher_champs_id_1.clear()
chercher_champs_id_1.send_keys(id_1)
chercher_champs_id_1.send_keys(Keys.ENTER)

time.sleep(3)
navigateur.find_element(By.ID,"8_btn").click()

time.sleep(5)
navigateur.find_element(By.ID,"3_btn").click()

