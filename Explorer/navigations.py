from Explorer.interface import afficher
import keyboard
from pathlib import Path
from Explorer.actions import paste, delete, rename
import time

def naviguer(path):
    selected_index = 0
    copy = ''
    action = 'paste'
    message = ''

    while True:
        try:
            files = list(Path(path).iterdir())
            afficher(path, selected_index , message)
            message = ''

            if not files:  # Si le dossier est vide
                selected_index = 0

            key = keyboard.read_event().name  # Attend une touche
            time.sleep(0.1)

            if key == "up" and selected_index > 0:
                selected_index -= 1
            elif key == "down" and selected_index < len(files) - 1:
                selected_index += 1
            elif key == "enter" and files:
                if files[selected_index].is_dir():
                    path = str(files[selected_index])
                    selected_index = 0
            elif key == 'esc':
                parent_path = str(Path(path).parent)
                if parent_path != path:
                    path = parent_path
                    selected_index = 0
            elif keyboard.is_pressed('shift+d') and files:
                message = delete(files[selected_index])
            elif keyboard.is_pressed('shift+r') and files:
                message = rename(files[selected_index])
            elif keyboard.is_pressed("shift+c") and files:
                copy = str(files[selected_index])
            elif keyboard.is_pressed("shift+v"):
                if copy:
                    message = paste(copy, str(path) , action)
                    copy = ''
                    if action == 'move':
                        action = 'paste'
                else:
                    message = 'Rien a coller'
            elif keyboard.is_pressed("shift+x") and files:
                copy = str(files[selected_index])
                action = 'move'

        except Exception as e:
            message = f"Erreur : {e}"
