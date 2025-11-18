import subprocess
import os


directory = r"C:\Users\Utilisateur\Desktop\AUTOMATISATION_EXTRACTIONS\COTE_DIVOIRE\UBIPHARM"

scripts = [
    "arkopharma.py",
    "bio_lab_ubi.py",
    "bioderma.py",
    "pfizer.py",
    "sandoz.py",
]

os.chdir(directory)

for script in scripts:
   
    print(f"Exécution de {script}...")
      
    subprocess.run(["python", script])
    
    print(f"{script} terminé.\n")
