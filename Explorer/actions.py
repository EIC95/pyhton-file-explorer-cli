# Importation des modules nécessaires
import shutil  # Pour la manipulation des fichiers et dossiers (copie, suppression, déplacement)
import os  # Pour la gestion des chemins et opérations sur les fichiers
import ctypes  # Pour afficher des boîtes de dialogue système (Windows uniquement)
from pathlib import Path  # Pour la gestion des chemins de fichiers et dossiers

def paste(path, destination, action):
    """
    Colle ou déplace un fichier/dossier vers un répertoire cible.
    
    Args:
        path (str): Chemin du fichier ou dossier source.
        destination (str): Chemin du dossier de destination.
        action (str): 'paste' pour copier, 'move' pour déplacer.
    
    Returns:
        str: Message indiquant le succès ou l'échec de l'opération.
    """
    try:
        # Vérification de l'existence des chemins source et destination
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
    """
    Supprime un fichier ou un dossier après confirmation de l'utilisateur.
    
    Args:
        path (str): Chemin du fichier ou dossier à supprimer.
    
    Returns:
        str: Message indiquant le succès ou l'échec de l'opération.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier ou dossier '{path}' n'existe pas.")

        # Boîte de confirmation Windows (1 = OK, 2 = Annuler)
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
    """
    Renomme un fichier ou un dossier.
    
    Args:
        path (str): Chemin du fichier ou dossier à renommer.
    
    Returns:
        str: Message indiquant le succès ou l'échec de l'opération.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier ou dossier '{path}' n'existe pas.")

        new_name = input("Nouveau nom : ")
        if not new_name:
            raise ValueError("Le nouveau nom ne peut pas être vide.")

        new_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_path)
        return 'Renommé'

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
    """
    Trie les fichiers et dossiers par type (dossiers en premier, puis fichiers par extension).
    
    Args:
        path (str): Chemin du dossier à trier.
    
    Returns:
        tuple: Liste triée et message de confirmation.
    """
    try:
        files = [f for f in Path(path).iterdir() if f.exists()]
        sorted_files = sorted(files, key=lambda f: (f.is_file(), f.suffix.lower()), reverse=True)
        return sorted_files, 'Trié par type'
    except Exception as e:
        return [], f"Erreur : {e}"

def sort_by_date(path):
    """
    Trie les fichiers et dossiers par date de modification (du plus récent au plus ancien).
    
    Args:
        path (str): Chemin du dossier à trier.
    
    Returns:
        tuple: Liste triée et message de confirmation.
    """
    try:
        files = []
        for f in Path(path).iterdir():
            try:
                files.append(f)  # Stocke uniquement le fichier
            except Exception:
                continue  # Ignore les erreurs et continue la boucle
        sorted_files = sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)
        return sorted_files, 'Trié par date'
    except Exception as e:
        return [], f"Erreur : {e}"

def sort_by_size(path):
    """
    Trie les fichiers et dossiers par taille (du plus grand au plus petit).
    
    Args:
        path (str): Chemin du dossier à trier.
    
    Returns:
        tuple: Liste triée et message de confirmation.
    """
    try:
        files = []
        for f in Path(path).iterdir():
            try:
                files.append(f)  # Stocke uniquement le fichier
            except Exception:
                continue  # Ignore les erreurs et continue la boucle
        sorted_files = sorted(files, key=lambda f: f.stat().st_size if f.is_file() else 0, reverse=True)
        return sorted_files, 'Trié par taille'
    except Exception as e:
        return [], f"Erreur : {e}"