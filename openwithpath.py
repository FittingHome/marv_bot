import os
import subprocess

def ouvrir_fichier_avec_application(path_fichier, application):
    if not os.path.isfile(path_fichier):
        print(f"Le fichier {path_fichier} n'existe pas.")
        return

    if not os.access(path_fichier, os.R_OK):
        print(f"Le fichier {path_fichier} n'est pas lisible.")
        return

    try:
        subprocess.Popen([application, path_fichier])
    except OSError as e:
        print(f"Erreur lors de l'ouverture de {path_fichier} avec {application}: {e}")
