import time
import platform

try:
    # Importation de la fonction principale de navigation
    from Explorer.navigations import naviguer
except ModuleNotFoundError:
    print("Erreur : Le module 'Explorer.navigations' est introuvable. Vérifiez que le fichier existe et que le chemin est correct.")
    print("Le programme va s'éteindre dans 1 minute...")
    time.sleep(60)
    exit(1)

# Déterminer le chemin de départ en fonction du système d'exploitation
systeme = platform.system()

if systeme == "Windows":
    path = "C:\\"
elif systeme == "Darwin":  # macOS
    path = "/Users"
elif systeme == "Linux":
    path = "/home"
else:
    print(f"Erreur : Système d'exploitation non reconnu ({systeme}).")
    print("Le programme va s'éteindre dans 1 minute...")
    time.sleep(60)
    exit(1)

try:
    # Démarrer la navigation depuis le chemin détecté
    naviguer(path)
except FileNotFoundError as e:
    print(f"Erreur : Le chemin spécifié est introuvable. Détails : {e}")
except PermissionError:
    print("Erreur : Accès refusé au répertoire de départ. Essayez d'exécuter le programme en mode administrateur.")
except Exception as e:
    print(f"Erreur inattendue : {e}")

print("Le programme va s'éteindre dans 1 minute...")
time.sleep(60)
