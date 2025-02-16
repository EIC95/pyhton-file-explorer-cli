from Explorer.interface import afficher
import keyboard
from pathlib import Path

def naviguer(path):
    selected_index = 0

    while True:
        files = list(Path(path).iterdir())
        afficher(path, selected_index)

        key = keyboard.read_event().name

        if key == "up" and selected_index > 0:
            selected_index -= 1
        elif key == "down" and selected_index < len(files) - 1:
            selected_index += 1
        elif key == "enter":
            if files[selected_index].is_dir():
                path = str(files[selected_index])
                selected_index = 0
        elif key == 'esc':
            parent_path = str(Path(path).parent)
            if parent_path != path:
                path = parent_path
                selected_index = 0