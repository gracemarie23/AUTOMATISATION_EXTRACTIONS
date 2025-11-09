from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import os
import time
import glob

load_dotenv()

#chemin_extractions_labell = "C:/Users/Utilisateur/Desktop/AUTOMATISATION_EXTRACTIONS/TEDIS/extractions/LABELL"
firefox_options = Options()

firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.dir", "C:\\Users\\Utilisateur\\Desktop\\AUTOMATISATION_EXTRACTIONS\\TEDIS\\extractions\\LABELL")
firefox_options.set_preference("browser.download.useDownloadDir", True)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", 
                              "text/csv,application/csv,application/vnd.ms-excel,application/octet-stream")
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("pdfjs.disabled", True)
firefox_options.set_preference("browser.download.manager.showAlertOnComplete", False)

service = Service("C:/Users/Utilisateur/Desktop/AUTOMATISATION_EXTRACTIONS/geckodriver.exe")
navigateur = webdriver.Firefox(service=service, options=firefox_options)
navigateur.maximize_window()

navigateur.get("https://www.tedispharma-ci.com/")

user_1 = os.getenv('user_ted_labell')
mdp_1  = os.getenv('mdp_ted_labell')

time.sleep(3)

chercher_champs_1 = navigateur.find_element(By.ID,"username")
chercher_champs_1.clear()
chercher_champs_1.send_keys(user_1)

chercher_champs_2 = navigateur.find_element(By.ID,"password")
chercher_champs_2.clear()
chercher_champs_2.send_keys(mdp_1)
chercher_champs_2.send_keys(Keys.ENTER)

time.sleep(15)
navigateur.find_element(By.ID,"btnExportCsv").click()
time.sleep(15)



