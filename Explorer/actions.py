import shutil
import os
import ctypes


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
