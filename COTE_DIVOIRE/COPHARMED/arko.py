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
import shutil
from datetime import datetime
load_dotenv()

PAYS = "COTE_DIVOIRE"
MOIS = datetime.now().strftime("%Y-%m")  
GROSSISTE = "COPHARMED"
LABORATOIRE = "ARKOPHARMA"  


base_path = "C:\\Users\\Utilisateur\\Desktop\\AUTOMATISATION_EXTRACTIONS\\DONNEES"
dossier_final = os.path.join(base_path, PAYS, MOIS, GROSSISTE, LABORATOIRE)
os.makedirs(dossier_final, exist_ok=True)

dossier_temp = os.path.join(base_path, "temp_downloads")
os.makedirs(dossier_temp, exist_ok=True)


for fichier in glob.glob(os.path.join(dossier_temp, "*")):
    try:
        os.remove(fichier)
    except:
        pass


firefox_options = Options()

firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.dir", dossier_temp)
firefox_options.set_preference("browser.download.useDownloadDir", True)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", 
                              "text/csv,application/csv,application/vnd.ms-excel,application/octet-stream")
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("pdfjs.disabled", True)
firefox_options.set_preference("browser.download.manager.showAlertOnComplete", False)

service = Service("C:/Users/Utilisateur/Desktop/AUTOMATISATION_EXTRACTIONS/geckodriver.exe")
navigateur = webdriver.Firefox(service=service, options=firefox_options)
navigateur.maximize_window()

navigateur.get("https://service02ab.eurapharma.com/cgiphl/pw_call.pgm?PGMA=VID020")

user_1 = os.getenv('user_co_arko')
mdp_1  = os.getenv('mdp_co_arko')
id_1 = os.getenv("id_6_co")
time.sleep(3)

chercher_champs_1 = navigateur.find_element(By.NAME,"name1")
chercher_champs_1.clear()
chercher_champs_1.send_keys(user_1)

chercher_champs_2 = navigateur.find_element(By.NAME,"name2")
chercher_champs_2.clear()
chercher_champs_2.send_keys(mdp_1)
chercher_champs_2.send_keys(Keys.ENTER)

time.sleep(7)


id_1 = id_1.strip().strip('"').strip("'") if id_1 else ""

chercher_champs_3 = navigateur.find_element(By.ID,"f1_4")

navigateur.execute_script("arguments[0].value = '';", chercher_champs_3)
time.sleep(0.5)
navigateur.execute_script("arguments[0].focus();", chercher_champs_3)
time.sleep(0.5)
navigateur.execute_script(f"arguments[0].value = '{id_1}';", chercher_champs_3)
time.sleep(0.5)
navigateur.execute_script("""
    var element = arguments[0];
    element.dispatchEvent(new Event('input', { bubbles: true }));
    element.dispatchEvent(new Event('change', { bubbles: true }));
    element.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
""", chercher_champs_3)

time.sleep(2)


navigateur.find_element(By.ID,"1_btn").click()

time.sleep(5)
navigateur.find_element(By.ID,"3_btn").click()
time.sleep(5)
navigateur.find_element(By.ID,"6_btn").click()
time.sleep(5)
navigateur.find_element(By.ID,"11_btn").click()
time.sleep(5)
navigateur.quit()


time.sleep(5)

fichiers_telecharges = glob.glob(os.path.join(dossier_temp, "*.*"))

for fichier in fichiers_telecharges:
    if os.path.isfile(fichier) and not fichier.endswith('.part'):  
        nom_fichier = os.path.basename(fichier)
        destination = os.path.join(dossier_final, nom_fichier)
        shutil.move(fichier, destination)