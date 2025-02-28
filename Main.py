import time

try:
    # Importation de la fonction principale de navigation depuis le module Explorer.navigations
    from Explorer.navigations import naviguer
except ModuleNotFoundError:
    print("Erreur : Le module 'Explorer.navigations' est introuvable. Vérifiez que le fichier existe et que le chemin est correct.")
    print("Le programme va s'éteindre dans 1 minute...")
    time.sleep(60)  # Pause de 60 secondes avant la fermeture
    exit(1)  # Quitte avec un code d'erreur

try:
    # Appel de la fonction naviguer avec le chemin de départ 'C:/'
    # Ce chemin représente le point d'entrée de l'explorateur de fichiers.
    # Il peut être modifié pour démarrer la navigation depuis un autre répertoire.
    naviguer('C:/')
except FileNotFoundError as e:
    print(f"Erreur : Le chemin spécifié est introuvable. Détails : {e}")
except PermissionError:
    print("Erreur : Accès refusé au répertoire de départ. Essayez d'exécuter le programme en mode administrateur.")
except Exception as e:
    print(f"Erreur inattendue : {e}")

print("Le programme va s'éteindre dans 1 minute...")
time.sleep(60)  # Pause de 60 secondes avant la fermeture
