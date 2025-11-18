import subprocess
import os


directory = r"C:\Users\Utilisateur\Desktop\AUTOMATISATION_EXTRACTIONS\SENEGAL\LABOREX"

scripts = [
    "bioderma_pfizer.py",
    "biofar.py",
    "labell_ubi.py",
    "sandoz.py",
]

os.chdir(directory)

for script in scripts:
   
    print(f"Exécution de {script}...")
      
    subprocess.run(["python", script])
    
    print(f"{script} terminé.\n")
