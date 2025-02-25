import shutil
import os
import ctypes
from pathlib import Path


def paste(path, destination, action):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier ou dossier '{path}' n'existe pas.")
        if not os.path.exists(destination):
            raise FileNotFoundError(f"Le dossier de destination '{destination}' n'existe pas.")

        if action == 'move':
            shutil.move(path, destination)
            return 'Déplacé'
        else:
            shutil.copytree(path, destination) if os.path.isdir(path) else shutil.copy(path, destination)
            return 'Collé'

    except FileNotFoundError as e:
        return f"Erreur : {e}"
    except PermissionError:
        return f"Erreur : Permission refusée pour accéder à '{path}'."
    except Exception as e:
        return f"Erreur inattendue : {e}"


def delete(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier ou dossier '{path}' n'existe pas.")

        if ctypes.windll.user32.MessageBoxW(0, f"Supprimer {path} ?", "Confirmation", 1) == 1:
            shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
            return 'Supprimé'

    except FileNotFoundError as e:
        return f"Erreur : {e}"
    except PermissionError:
        return f"Erreur : Impossible de supprimer '{path}', accès refusé."
    except Exception as e:
        return f"Erreur inattendue : {e}"


def rename(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier ou dossier '{path}' n'existe pas.")

        new_name = input("Nouveau nom : ")
        if not new_name:
            raise ValueError("Le nouveau nom ne peut pas être vide.")

        new_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_path)
        return 'renommé'


    except FileNotFoundError as e:
        return f"Erreur : {e}"
    except FileExistsError:
        return f"Erreur : Un fichier ou dossier avec ce nom existe déjà."
    except PermissionError:
        return f"Erreur : Impossible de renommer '{path}', accès refusé."
    except ValueError as e:
        return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur inattendue : {e}"
def sort_by_type(path):
    try:
        files = [f for f in Path(path).iterdir() if f.exists()]
        sorted_files = sorted(files, key=lambda f: (f.is_file(), f.suffix.lower()), reverse=True)
        return sorted_files, 'Trié par type'
    except Exception as e:
        return [], f"Erreur : {e}"

def sort_by_date(path):
    try:
        files = []
        for f in Path(path).iterdir():
            try:
                files.append(f)  # On stocke juste le fichier, pas un tuple
            except Exception:
                continue
        sorted_files = sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)
        return sorted_files, 'Trié par date'
    except Exception as e:
        return [], f"Erreur : {e}"

def sort_by_size(path):
    try:
        files = []
        for f in Path(path).iterdir():
            try:
                files.append(f)  # On stocke juste le fichier, pas un tuple
            except Exception:
                continue
        sorted_files = sorted(files, key=lambda f: f.stat().st_size if f.is_file() else 0, reverse=True)
        return sorted_files, 'Trié par taille'
    except Exception as e:
        return [], f"Erreur : {e}"



