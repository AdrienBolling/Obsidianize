# Here we set up our entrypoints for the CLI.
import os
import sys

import fire

from obsidianize.scripts.convert import convert_all_notebooks_to_md, convert_notebook_to_md
from obsidianize.scripts.setup import setup_git_hooks, setup_git_ignore_md, setup_git_ignore_assets


class Obsidianize:
    def __init__(self):
        pass

    def setup(
            self,
            path: str = "./",
            which_hook: str = "pre-commit",
            hook: str = "default",
            ignore_md: bool = True,
            ignore_assets: bool = True,
    ):
        """
        This function sets up the git repository located at path to use the obsidianize package.
        :param path: str: path to the git repository to set up
        :param which_hook: str: to specify which hook to set up (pre-commit by default, recommended)
        :param hook: str: to specify which hook content from the json file to use (default by default, nothing else
        implemented)
        :param ignore_md: bool: add .md files to .gitignore (except README.md) (True by default)
        :param ignore_assets: bool: add assets folder to .gitignore (True by default)
        :return: nothing (will convert the files in place)
        """

        setup_git_hooks(path, which_hook, hook)
        if ignore_md:
            setup_git_ignore_md(path)
        if ignore_assets:
            setup_git_ignore_assets(path)
        # Make the path absolute
        path = os.path.abspath(path)
        print(f"git repository (at {path}) set up to use the obsidianize package")

    def convert(
            self,
            path: str = "./"
    ):
        """
        This function converts a jupyter notebook, or a folder of jupyter notebooks to a markdown file.
        :param path: str: path to the file to convert
        :return: nothing (will convert the file in place)
        """
        # Check if the path is a file
        if os.path.isfile(path):

            # Check if the file is a jupyter notebook
            if path.endswith(".ipynb"):
                convert_notebook_to_md(path)
            else:
                raise ValueError("This file is not a jupyter notebook")

        # Check if the path is a directory
        elif os.path.isdir(path):
            convert_all_notebooks_to_md(path)
        else:
            raise ValueError("path should lead to a .ipynb file or a folder")

        # Make the path absolute
        path = os.path.abspath(path)
        print(f"{path} converted to markdown")

    def refresh(
            self,
            path: str = "./"
    ):
        """
        This function refreshes the markdown files in a folder.
        :param path: str: path to the folder to refresh
        :return: nothing (will convert the files in place)
        """
        # If path does not exist, assume the file has been deleted in the commit
        # in this case we still want to keep the assets as to not lose them in the obsidian notes
        if not os.path.exists(path):
            print(f"{path} does not exist")
            return
        # Check if the path is a directory or a .ipynb file
        if os.path.isdir(path):
            convert_all_notebooks_to_md(path)
        elif path.endswith(".ipynb"):
            convert_notebook_to_md(path)

        # Make the path absolute
        path = os.path.abspath(path)
        print(f"{path} refreshed")

    def help(
            self,
            function: str = ""
    ):
        """
        This function prints the help message.
        :return: nothing
        """
        if function == "setup":
            print(self.setup.__doc__)
        elif function == "convert":
            print(self.convert.__doc__)
        elif function == "refresh":
            print(self.refresh.__doc__)
        else:
            print("Available functions:")
            print(self.setup.__doc__)
            print(self.convert.__doc__)
            print(self.refresh.__doc__)


def main_cli():
    fire.Fire(Obsidianize)


if __name__ == "__main__":
    main_cli()
