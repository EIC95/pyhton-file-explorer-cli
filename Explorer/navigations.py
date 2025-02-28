from Explorer.interface import afficher
import keyboard
from Explorer.actions import *
import time

def naviguer(path):
    selected_index = 0
    copy = ''
    action = 'paste'
    message = ''
    files = list(Path(path).iterdir())

    while True:
        try:
            if not files:
                files = list(Path(path).iterdir())

            afficher(files, path, selected_index, message)
            message = ''

            if not files:  # Si le dossier est vide
                selected_index = 0

            key = keyboard.read_event().name  # Attend une touche

            if key == "up" and selected_index > 0:
                selected_index -= 1
            elif key == "down" and selected_index < len(files) - 1:
                selected_index += 1
            elif key == "enter" and files:
                if files[selected_index].is_dir():
                    path = str(files[selected_index])
                    selected_index = 0
                    files = list(Path(path).iterdir())  # Mettre à jour la liste des fichiers
            elif key == 'esc':
                parent_path = str(Path(path).parent)
                if parent_path != path:
                    path = parent_path
                    selected_index = 0
                    files = list(Path(path).iterdir())  # Mise à jour après retour
            elif key == 'shift' and files:
                time.sleep(0.2)
                combi = keyboard.read_event().name
                if combi == "d":
                    message = delete(files[selected_index])
                    files = list(Path(path).iterdir())  # Mettre à jour après suppression
                elif combi == 'r':
                    time.sleep(0.1)
                    message = rename(files[selected_index])
                    files = list(Path(path).iterdir())  # Mettre à jour après renommage
                elif combi == 'c':
                    copy = str(files[selected_index])
                    message = 'Copié'
                elif combi == 'v':
                    if copy:
                        message = paste(copy, str(path), action)
                        copy = ''
                        if action == 'move':
                            action = 'paste'
                        files = list(Path(path).iterdir())  # Mise à jour après collage
                    else:
                        message = 'Rien à coller'
                elif combi == 'x':
                    copy = str(files[selected_index])
                    message = 'Coupé'
                    action = 'move'
                elif combi == 'k':
                    files, message = sort_by_type(path)
                elif combi == 's':
                    files, message = sort_by_size(path)
                elif combi == 't':
                    files, message = sort_by_date(path)

        except Exception as e:
            message = f"Erreur : {e}"
            afficher(files, path, selected_index, message)  # Afficher l'erreur
            print("\nAppuyez sur une touche pour continuer...")
            keyboard.read_event()  # Attendre une touche pour éviter la boucle infinie
            message = ''  # Réinitialiser le message pour ne pas le voir en boucle
