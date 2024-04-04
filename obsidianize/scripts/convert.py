"""
This script converts one or several Jupyter notebook to an Obsidian markdown file.
To convert a single notebook, run with a file path as argument.
To convert all notebooks in a folder, run with the folder path as argument.
Run the following command in the terminal:
obsidianize path
"""

import os
import sys
from pathlib import Path

import nbformat
import fire

from obsidianize.src.utils.path_utils import get_repo_path
from obsidianize.src.utils.to_markdown import convert_to_markdown
from obsidianize.src.utils.format_md import format_markdown
from obsidianize.src.utils.save_md import save_markdown


def main(
        path: str
):
    """
    Function to convert a jupyter notebook to a markdown file.
    Or to convert all the jupyter notebooks in a folder to markdown files.
    :param path: str: path to the file or folder to convert
    :return: nothing, will convert the files in place
    """

    if os.path.isfile(path) and path.endswith(".ipynb"):
        convert_notebook_to_md(path)
    elif os.path.isdir(path):
        convert_all_notebooks_to_md(path)
    else:
        raise ValueError("path should lead to a .ipynb file or a folder")


def convert_notebook_to_md(path: str):
    """
    Function to convert a jupyter notebook to a markdown file.
    :param path:
    :return:
    """
    # Get the cwd
    cwd = Path.cwd()
    # # Check if the cwd is a repository (check presence of .git with Path)
    # if not Path(cwd / ".git").is_dir():
    #     cwd = Path(get_repo_path(str(cwd)))
    # Resolve the path to make it absolute
    path = str(cwd / Path(path))

    # Check if the path exists, if not do nothing
    if not os.path.exists(path):
        return
    # Check if the path is a file
    if not os.path.isfile(path):
        raise ValueError("path should lead to a file")
    # Check if the file is a jupyter notebook
    if not path.endswith(".ipynb"):
        raise ValueError("path should lead to a jupyter notebook")

    # Load the notebook
    with open(path, "r") as f:
        notebook = nbformat.read(f, as_version=4)

    # Convert the notebook to markdown
    markdown = convert_to_markdown(notebook)

    # Format the markdown
    markdown = format_markdown(markdown, path)

    # Save the markdown
    save_markdown(markdown, path)


def convert_all_notebooks_to_md(folder: str):
    """
    Function to convert all the jupyter notebooks in a folder to markdown files.
    :param folder:
    :return:
    """

    # Check if the path exists, if not do nothing
    if not os.path.exists(folder):
        return

    # Check if the path is a folder
    if not os.path.isdir(folder):
        raise ValueError("path should lead to a folder")

    # Get all the files in the folder
    files = os.listdir(folder)
    # Filter the files to keep only the jupyter notebooks
    notebooks = [f for f in files if f.endswith(".ipynb")]

    # Convert each notebook to markdown
    for notebook in notebooks:
        convert_notebook_to_md(os.path.join(folder, notebook))


def main_cli():
    fire.Fire(main)
