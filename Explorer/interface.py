# Importation des modules nécessaires
import datetime  # Pour la gestion des dates et la conversion des timestamps
import os , platform  # Pour la gestion du terminal (effacer l'écran, vérifier le système d'exploitation)
from pathlib import Path  # Pour la gestion des chemins de fichiers et dossiers

def format_size(size_in_bytes):
    """
    Convertit une taille en octets en une unité plus lisible (Ko, Mo, Go, To).
    
    Args:
        size_in_bytes (int): Taille en octets.
    
    Returns:
        str: Taille formatée sous forme de chaîne avec l'unité appropriée.
    """
    try:
        for unit in ['B', 'Ko', 'Mo', 'Go']:  # Liste des unités
            if size_in_bytes < 1024:  # Si la taille est inférieure à 1024, on affiche l'unité actuelle
                return f"{size_in_bytes:.1f} {unit}"
            size_in_bytes /= 1024  # Conversion vers l'unité supérieure
        return f"{size_in_bytes:.1f} To"  # Si la taille dépasse le Go, on l'affiche en To (Téraoctets)
    except Exception as e:
        return f"Erreur : {e}"

def format_date(timestamp):
    """
    Convertit un timestamp en une date lisible.
    
    Args:
        timestamp (float): Timestamp du fichier (modification).
    
    Returns:
        str: Date formatée sous la forme "JJ/MM/AAAA HH:MM".
    """
    try:
        return datetime.datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")
    except Exception as e:
        return f"Erreur : {e}"

def clear_screen():
    """
    Efface l'écran du terminal en fonction du système d'exploitation.
    """
    try:
        os.system("cls" if platform.system() == "Windows" else "clear")
    except Exception as e:
        print(f"Erreur lors de l'effacement de l'écran : {e}")

def afficher(files, path, selected_item, message):
    """
    Affiche la liste des fichiers et dossiers dans le terminal avec leur nom, type, taille et date de modification.
    
    Args:
        files (list): Liste des fichiers et dossiers du répertoire courant.
        path (str): Chemin du répertoire actuel.
        selected_item (int): Index de l'élément actuellement sélectionné.
        message (str): Message d'information ou d'erreur à afficher à l'utilisateur.
    """
    try:
        # Effacer l'écran avant d'afficher le contenu mis à jour
        clear_screen()

        # Vérification que le chemin existe
        if not Path(path).exists():
            print(f"Erreur : Le chemin '{path}' n'existe pas.")
            return

        # Affichage du chemin actuel
        print('Chemin : ' + path)
        print("=" * 75)

        # En-tête du tableau
        print(f"{'...':<2} {'Nom':<33} {'Type':<10} {'Taille':<10} {'Modifié le'}")
        print("=" * 75)

        # Boucle sur la liste des fichiers et dossiers
        for index, item in enumerate(files):
            try:
                # Vérifier si l'élément est un fichier ou un dossier
                file_type = "Fichier" if item.is_file() else "Dossier"
                # Obtenir la taille si c'est un fichier, sinon afficher "—"
                size = format_size(item.stat().st_size) if item.is_file() else "—"
                # Obtenir la date de dernière modification
                mod_date = format_date(item.stat().st_mtime)

                # Mise en évidence de l'élément sélectionné
                if index == selected_item:
                    print(f" *  {item.name:<30} {file_type:<10} {size:<10} {mod_date}")
                else:
                    print(f"    {item.name:<30} {file_type:<10} {size:<10} {mod_date}")
            except PermissionError:
                print(f"    {item.name:<30} {'Accès refusé':<10} {'—':<10} {'—'}")
            except FileNotFoundError:
                print(f"    {item.name:<30} {'Introuvable':<10} {'—':<10} {'—'}")
            except Exception as e:
                print(f"    {item.name:<30} {'Erreur':<10} {'—':<10} {e}")

        print("=" * 75)

        # Instructions pour l'utilisateur
        print('Appuyez sur la flèche du haut et celle du bas pour vous déplacer dans un dossier')
        print('Appuyez sur Entrée pour entrer dans un dossier')
        print('Appuyez sur Echap pour quitter un dossier')
        print('Appuyez sur Shift + C pour copier')
        print('Appuyez sur Shift + V pour coller')
        print('Appuyez sur Shift + X puis déplacez-vous dans le dossier cible et appuyez sur Shift + V pour déplacer')
        print('Appuyez sur Shift + R pour renommer')
        print('Appuyez sur Shift + K pour trier par type')
        print('Appuyez sur Shift + T pour trier par date')
        print('Appuyez sur Shift + S pour trier par taille')
        print("Appuyez sur Shift + Echap pour quitter l'application")

        print('=' * 75)

        # Affichage du message d'information ou d'erreur s'il y en a un
        print(message)
    except Exception as e:
        print(f"Erreur lors de l'affichage : {e}")
