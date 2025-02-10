from pathlib import Path
import datetime

def format_size(size_in_bytes):
    for unit in ['B', 'Ko', 'Mo', 'Go']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.1f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.1f} To"

def format_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")

def afficher(path):
    repertoire = Path(path)

    print(f"{'Nom':<33} {'Type':<10} {'Taille':<10} {'Modifié le'}")
    print("=" * 72)

    for item in repertoire.iterdir():
        if item.is_file():
            icon = "📄"
            file_type = "Fichier"
        else:
            file_type = "Dossier"
            icon = "📁"
        size = format_size(item.stat().st_size) if item.is_file() else "—"
        mod_date = format_date(item.stat().st_mtime)

        print(f"{icon} {item.name:<30} {file_type:<10} {size:<10} {mod_date}")

