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

chemin_extraction_biofar = "C:/Users/Utilisateur/Desktop/AUTOMATISATION_EXTRACTIONS/TEDIS/extractions/BIOFAR"

# Créer le dossier s'il n'existe pas
os.makedirs(chemin_extraction_biofar, exist_ok=True)

# Configuration Firefox (remplace chrome_options)
firefox_options = Options()

# Préférences de téléchargement pour Firefox
firefox_options.set_preference("browser.download.folderList", 2)  # 2 = dossier personnalisé
firefox_options.set_preference("browser.download.dir", chemin_extraction_biofar)
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("browser.download.useDownloadDir", True)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", 
                              "text/csv,application/csv,application/vnd.ms-excel,application/octet-stream")
firefox_options.set_preference("browser.download.manager.showAlertOnComplete", False)
firefox_options.set_preference("pdfjs.disabled", True)

# Désactiver les notifications
firefox_options.set_preference("dom.webnotifications.enabled", False)
firefox_options.set_preference("dom.push.enabled", False)

# Désactiver la demande de sauvegarde des mots de passe
firefox_options.set_preference("signon.rememberSignons", False)
firefox_options.set_preference("signon.autofillForms", False)

# Lancer Firefox avec webdriver-manager
service = Service(GeckoDriverManager().install())
navigateur = webdriver.Firefox(service=service, options=firefox_options)

# Maximiser la fenêtre
navigateur.maximize_window()

print("🦊 Firefox lancé avec succès!")
print(f"📁 Dossier de téléchargement : {chemin_extraction_biofar}")

navigateur.get("https://www.tedispharma-ci.com/")

user_1 = os.getenv('user_ted_biofar')
mdp_1 = os.getenv('mdp_ted_biofar')

time.sleep(3)

chercher_champs_1 = navigateur.find_element(By.ID, "username")
chercher_champs_1.clear()
chercher_champs_1.send_keys(user_1)

chercher_champs_2 = navigateur.find_element(By.ID, "password")
chercher_champs_2.clear()
chercher_champs_2.send_keys(mdp_1)
chercher_champs_2.send_keys(Keys.ENTER)

print("Connexion effectuée, attente de 30 secondes...")
time.sleep(30)

# Compter les fichiers avant téléchargement
fichiers_avant = set(os.listdir(chemin_extraction_biofar))
print(f"📊 Fichiers avant téléchargement : {len(fichiers_avant)}")

# Cliquer sur le bouton d'export
print("🖱️ Clic sur le bouton d'export...")
btn_export = navigateur.find_element(By.ID, "btnExportCsv")
navigateur.execute_script("arguments[0].click();", btn_export)

# Attendre que le spinner apparaisse
try:
    wait = WebDriverWait(navigateur, 10)
    spinner = wait.until(EC.presence_of_element_located((By.ID, "checkSpinner")))
    print("✓ Téléchargement démarré (spinner détecté)")
except:
    print("⚠ Spinner non détecté, poursuite...")

# Attendre que le spinner disparaisse
try:
    wait = WebDriverWait(navigateur, 120)
    wait.until(lambda driver: driver.find_element(By.ID, "checkSpinner").get_attribute("aria-hidden") == "true")
    print("✓ Spinner disparu, téléchargement terminé")
except Exception as e:
    print(f"⚠ Timeout spinner : {e}")

# Attendre que le fichier apparaisse
print("⏳ Attente du fichier (max 60 secondes)...")
timeout = 60
start_time = time.time()
fichier_trouve = None

while time.time() - start_time < timeout:
    try:
        fichiers_apres = set(os.listdir(chemin_extraction_biofar))
        nouveaux = fichiers_apres - fichiers_avant
        
        # Vérifier les nouveaux fichiers CSV (ignorer les .part de Firefox)
        nouveaux_csv = [f for f in nouveaux if f.endswith('.csv') and not f.endswith('.part')]
        
        if nouveaux_csv:
            fichier_trouve = nouveaux_csv[0]
            print(f"✅ Fichier téléchargé : {fichier_trouve}")
            break
    except:
        pass
    
    time.sleep(1)

if not fichier_trouve:
    print("❌ Aucun fichier téléchargé")
    fichiers_finaux = os.listdir(chemin_extraction_biofar)
    print(f"Fichiers dans le dossier : {fichiers_finaux}")
else:
    print(f"🎉 Téléchargement réussi en {int(time.time() - start_time)} secondes")

time.sleep(3)
#navigateur.quit()