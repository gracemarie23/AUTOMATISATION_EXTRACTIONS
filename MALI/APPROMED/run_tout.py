import subprocess
import os

directory = r"C:\Users\Utilisateur\Desktop\AUTOMATISATION_EXTRACTIONS\MALI\APPROMED"
scripts = [
    "biofar.py",
   "ubigen_lab.py"
]
os.chdir(directory)
for script in scripts:
    print(f"     Exécution de {script}...")
    subprocess.run(["python", script])
    print(f"{script} terminé.\n")
