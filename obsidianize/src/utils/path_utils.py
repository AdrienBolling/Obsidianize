import os
from time import sleep

import IPython
from pathlib import Path


def get_notebook_path() -> str:
    """
    Function to get the path to the current notebook.
    :return: str: the path to the current notebook
    """
    try:
        depth = 0
        while True:
            local = IPython.extract_module_locals(depth)[1]
            if '__session__' in local:
                # Get the notebook name if it is a Jupyter / Jupyterlab / JetBrains IDE session
                return local['__session__']
            elif '__vsc_ipynb_file__' in local:
                # Get the notebook name if it is a VSCode session
                return local['__vsc_ipynb_file__']
            else:
                depth += 1
    except Exception:
        raise Exception("Interpreter error, try using VSCode, Jupyter, Jupyterlab, or a JetBrains IDE")


def get_assets_path(path_to_notebook: str) -> str:
    """
    Function to get the path to the assets folder from the path of the notebook and the repository path.
    It navigates up the directory tree to find the .git directory, then constructs a path to the assets
    folder by appending 'assets' and the relative path from the repository root to the notebook's directory.

    :param path_to_notebook: Absolute path to the notebook.
    :return: Absolute path to the assets subfolder relative to the notebook's location.
    """
    # Get the cwd
    cwd = Path.cwd()
    # Check if the cwd is a repository (check presence of .git with Path)
    if not Path(cwd / ".git").is_dir():
        cwd = Path(get_repo_path(str(cwd)))
    # Resolve the path to make it absolute
    path_to_notebook = cwd / Path(path_to_notebook)
    path_to_repo = path_to_notebook.parent

    # Navigate up to find the .git directory indicating the repo root.
    while not (path_to_repo / ".git").exists():
        if path_to_repo.parent == path_to_repo:
            raise Exception(".git directory not found, are you sure this is a git repository?")
        path_to_repo = path_to_repo.parent

    # Calculate the relative path from the repo to the notebook

    relpath_to_notebook = path_to_notebook.relative_to(path_to_repo)

    # The assets directory is in the root with a subdirectory structure mirroring that of the notebook
    assets_path = path_to_repo / "assets" / relpath_to_notebook.parent
    assets_path.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
    return str(assets_path)


def in_obsidian_env() -> bool:
    """
    Function to check if the current environment is an Obsidian environment.
    :return: bool: True if the current environment is an Obsidian environment, False otherwise
    """
    try:
        depth = 0
        while True:
            local = IPython.extract_module_locals(depth)[1]
            if '__obsidian_execute_code_temp_pyplot_var__' in local:
                return True
            else:
                depth += 1
    except ValueError:
        return False


def get_vault_root(notebook_path) -> str:
    """
    Function to get the root of the vault.
    :param notebook_path: str: the path of the notebook
    :return: str: the root of the vault
    """

    # Get the path to the notebook
    path_to_notebook = Path(notebook_path)
    # Climb up the directory tree until we find the vault root (will contain .obsidian folder)
    while not (path_to_notebook / ".obsidian").exists():
        path_to_notebook = path_to_notebook.parent
    return str(path_to_notebook)


def get_repo_path(notebook_path: str) -> str:
    """
    Function to get the path to the repository.
    :param notebook_path: str: the path of the notebook
    :return: str: the path to the repository
    """

    # Get the path to the notebook
    path_to_notebook = Path(notebook_path)
    # Climb up the directory tree until we find the .git folder (will contain .git folder)
    while not (path_to_notebook / ".git").exists():
        path_to_notebook = path_to_notebook.parent

    return str(path_to_notebook)
