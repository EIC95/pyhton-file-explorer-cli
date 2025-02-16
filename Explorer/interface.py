from pathlib import Path
import datetime
import os

def format_size(size_in_bytes):
    for unit in ['B', 'Ko', 'Mo', 'Go']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.1f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.1f} To"

def format_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def afficher(path , selected_item):
    files = list(Path(path).iterdir())

    clear_screen()
    print(f"{'...':<2} {'Nom':<33} {'Type':<10} {'Taille':<10} {'Modifié le'}")
    print("=" * 75)

    for index, item in enumerate(files):
        if item.is_file():
            file_type = "Fichier"
        else:
            file_type = "Dossier"
        size = format_size(item.stat().st_size) if item.is_file() else "—"
        mod_date = format_date(item.stat().st_mtime)

        if index == selected_item:
            print(f" *  {item.name:<30} {file_type:<10} {size:<10} {mod_date}")
        else:
            print(f"    {item.name:<30} {file_type:<10} {size:<10} {mod_date}")

    return files




