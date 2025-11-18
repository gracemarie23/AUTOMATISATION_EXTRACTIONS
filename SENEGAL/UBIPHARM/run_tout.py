import subprocess
import os


directory = r"C:\Users\Utilisateur\Desktop\AUTOMATISATION_EXTRACTIONS\SENEGAL\UBIPHARM"

scripts = [
    "arkopharma.py",
    "biofar_labell_ubi.py",
    "pfizer.py",
    "sandoz.py",
    "ubigen.py",
]

os.chdir(directory)

for script in scripts:
   
    print(f"Exécution de {script}...")
      
    subprocess.run(["python", script])
    
    print(f"{script} terminé.\n")
