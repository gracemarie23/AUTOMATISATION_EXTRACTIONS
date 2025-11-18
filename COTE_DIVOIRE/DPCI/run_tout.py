import subprocess
import os

directory = r"C:\Users\Utilisateur\Desktop\AUTOMATISATION_EXTRACTIONS\COTE_DIVOIRE\DPCI"

scripts = [
    "b_l_u.py",
    "bioderm_p.py",
    "exphar.py",
    "sandoz.py",
]

os.chdir(directory)

for script in scripts:
   
    print(f"Exécution de {script}...")
    
    subprocess.run(["python", script])
    
    print(f"{script} terminé.\n")
