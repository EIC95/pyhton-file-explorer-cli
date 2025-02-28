# Importation de la fonction afficher pour afficher les fichiers et dossiers
from Explorer.interface import afficher
# Importation de la bibliothèque keyboard pour la gestion des entrées clavier
import keyboard
# Importation des fonctions d'actions pour gérer les fichiers (suppression, renommage, copie, etc.)
from Explorer.actions import *
# Importation du module time pour gérer certaines pauses dans l'exécution
import time
# Importation du module Path depuis pathlib pour la manipulation des chemins de fichiers
from pathlib import Path

def naviguer(path):
    """
    Fonction principale permettant la navigation dans l'explorateur de fichiers.

    Args:
        path (str): Chemin du répertoire à explorer.

    Fonctionnalités :
    - Affiche la liste des fichiers et dossiers.
    - Permet de naviguer avec les flèches haut/bas.
    - Ouvre un dossier avec 'Enter'.
    - Revient au dossier parent avec 'Esc'.
    - Effectue des actions sur les fichiers avec 'Shift' + une touche spécifique.
    """

    # Index de l'élément sélectionné dans la liste des fichiers
    selected_index = 0
    # Variable pour stocker un fichier copié ou coupé
    copy = ''
    # Indique si l'action en attente est un "coller" ou un "déplacer"
    action = 'paste'
    # Message d'information affiché à l'utilisateur
    message = ''
    # Récupération de la liste des fichiers et dossiers du chemin donné
    files = list(Path(path).iterdir())

    while True:
        try:
            # Vérifier si le dossier est vide et recharger les fichiers si nécessaire
            if not files:
                files = list(Path(path).iterdir())

            # Afficher l'interface avec la liste des fichiers, le chemin actuel et le message
            afficher(files, path, selected_index, message)
            message = ''  # Réinitialisation du message après affichage

            # Si le dossier est vide, réinitialiser l'index sélectionné
            if not files:
                selected_index = 0

            # Lecture d'un événement clavier (attente d'une touche)
            key = keyboard.read_event().name  

            # Navigation dans la liste des fichiers avec les flèches
            if key == "up" and selected_index > 0:
                selected_index -= 1
            elif key == "down" and selected_index < len(files) - 1:
                selected_index += 1

            # Entrer dans un dossier lorsqu'on appuie sur "Enter"
            elif key == "enter" and files:
                if files[selected_index].is_dir():  # Vérifier si c'est un dossier
                    path = str(files[selected_index])  # Mise à jour du chemin
                    selected_index = 0  # Réinitialisation de l'index
                    files = list(Path(path).iterdir())  # Recharger les fichiers

            # Retour au dossier parent avec "Esc"
            elif key == 'esc':
                parent_path = str(Path(path).parent)
                if parent_path != path:  # Vérifier qu'on n'est pas déjà à la racine
                    path = parent_path  # Mise à jour du chemin
                    selected_index = 0  # Réinitialisation de l'index
                    files = list(Path(path).iterdir())  # Mise à jour de la liste

            # Gestion des actions avec la touche "Shift" combinée à une autre touche
            elif key == 'shift' and files:
                time.sleep(0.2)  # Pause pour éviter la détection multiple
                combi = keyboard.read_event().name  # Lire la touche combinée

                if combi == "d":  # Suppression d'un fichier/dossier
                    message = delete(files[selected_index])
                    files = list(Path(path).iterdir())  # Mettre à jour la liste

                elif combi == 'r':  # Renommage d'un fichier/dossier
                    time.sleep(0.1)  # Petite pause pour éviter un double appel
                    message = rename(files[selected_index])
                    files = list(Path(path).iterdir())  # Mettre à jour la liste

                elif combi == 'c':  # Copier un fichier/dossier
                    copy = str(files[selected_index])
                    message = 'Copié'

                elif combi == 'v':  # Coller le fichier/dossier copié
                    if copy:
                        message = paste(copy, str(path), action)
                        copy = ''  # Réinitialisation après collage
                        if action == 'move':  # Si c'était un déplacement, réinitialiser l'action
                            action = 'paste'
                        files = list(Path(path).iterdir())  # Mise à jour de la liste
                    else:
                        message = 'Rien à coller'

                elif combi == 'x':  # Couper un fichier/dossier (déplacement)
                    copy = str(files[selected_index])
                    message = 'Coupé'
                    action = 'move'

                # Tri des fichiers selon différents critères
                elif combi == 'k':  # Trier par type de fichier
                    files, message = sort_by_type(path)

                elif combi == 's':  # Trier par taille
                    files, message = sort_by_size(path)

                elif combi == 't':  # Trier par date de modification
                    files, message = sort_by_date(path)

        except Exception as e:
            # Gestion des erreurs
            message = f"Erreur : {e}"
            afficher(files, path, selected_index, message)  # Affichage de l'erreur
            print("\nAppuyez sur une touche pour continuer...")
            keyboard.read_event()  # Pause pour éviter la boucle infinie
            message = ''  # Réinitialiser le message d'erreur pour la prochaine itération