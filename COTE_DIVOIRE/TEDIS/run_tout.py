import subprocess
import os


directory = r"C:\Users\Utilisateur\Desktop\AUTOMATISATION_EXTRACTIONS\COTE_DIVOIRE\TEDIS"

scripts = [
    "bioderma.py",
    "biofar.py",
    "exphar.py",
    "labell.py",
    "pfizer.py",
    "sandoz.py",
    "ubigen.py"
]

os.chdir(directory)

for script in scripts:
   
    print(f"Exécution de {script}...")
      
    subprocess.run(["python", script])
    
    print(f"{script} terminé.\n")
