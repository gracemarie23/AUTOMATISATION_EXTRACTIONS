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



PAYS = "Cote_d_Ivoire"
MOIS = datetime.now().strftime("%Y-%m")  
GROSSISTE = "UBIPHARM"
LABORATOIRE = "SANDOZ"  


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






#chemin_extractions_sandoz = "C:/Users/Utilisateur/Desktop/AUTOMATISATION_EXTRACTIONS/TEDIS/extractions/SANDOZ"
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

navigateur.get("https://fournisseur-cotedivoire.ubipharm.com/")

user_1 = os.getenv('user_ubi_exphar')
mdp_1  = os.getenv('mdp_ubi_exphar')

time.sleep(3)

chercher_champs_1 = navigateur.find_element(By.NAME,"Login")
chercher_champs_1.clear()
chercher_champs_1.send_keys(user_1)

chercher_champs_2 = navigateur.find_element(By.NAME,"Password")
chercher_champs_2.clear()
chercher_champs_2.send_keys(mdp_1)
chercher_champs_2.send_keys(Keys.ENTER)

time.sleep(10)
navigateur.find_element(By.LINK_TEXT, "Statistiques de Ventes").click()
time.sleep(10)
navigateur.find_element(By.CLASS_NAME,"exportcsv").click()
time.sleep(10)

navigateur.quit()

time.sleep(5)

fichiers_telecharges = glob.glob(os.path.join(dossier_temp, "*.*"))

for fichier in fichiers_telecharges:
    if os.path.isfile(fichier) and not fichier.endswith('.part'):  
        nom_fichier = os.path.basename(fichier)
        destination = os.path.join(dossier_final, nom_fichier)
        shutil.move(fichier, destination)