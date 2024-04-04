"""
This file contains the function used to set up the git repository to use the jupyter_displays_for_obsidian package.
It will implement a setup function used as a console script to set up the git repository.
To use it, run the following command in the terminal:
setup_jupyter_to_obsidian path
"""

import json
import os
from pathlib import Path

import fire


def main(
        path: str = "./",
        which: str = "pre-commit",
        hook: str = "default",
        ignore_md: bool = True,
):
    """
    Main function to set up the git repository to use the jupyter_displays_for_obsidian package.
    It will add a pre-commit hook that will convert the jupyter notebooks to markdown files.
    :param path: str: path to the folder to set up the git hooks
    :param which: str: to specify which hook to set up
    :param hook: str: to specify which hook content from the json file to use
    :param ignore_md: bool: add .md files to .gitignore (except README.md)
    :return: nothing, will convert the files in place
    """

    setup_git_hooks(path, which, hook)
    if ignore_md:
        setup_git_ignore(path)


def setup_git_hooks(path: str, which: str = "pre-commit", hook: str = "default"):
    """
    Function to set up the git hooks, by adding a pre-commit hook that will convert the jupyter notebooks to markdown files.
    :param path: str: path to the folder to set up the git hooks
    :param which: str: to specify which hook to set up
    :param hook: str: to specify which hook content from the json file to use
    :return: nothing, will convert the files in place
    """

    # Get path of the current file
    file_folder = Path(__file__).parent
    # Get path of the hooks.json file
    hooks_path = os.path.join(file_folder, "hooks.json")
    # Load the hook content (in the json file)
    with open(hooks_path, "r") as f:
        hooks = json.load(f)
    # Check if the hook is in the json file
    if hook not in hooks:
        raise ValueError(f"{hook} is not a valid hook")
    hook_content = hooks[hook]

    # Check if the path is a directory
    if not os.path.isdir(path):
        raise ValueError("path should lead to a folder")
    # Check if the path is a git repository
    if not os.path.isdir(os.path.join(path, ".git")):
        raise ValueError("path should lead to a git repository")
    # Check if the hook is already set up
    hook_path = os.path.join(path, ".git", "hooks", which)
    if os.path.isfile(hook_path):
        # Add the hook to the existing one
        with open(hook_path, "r") as f:
            existing_hook = f.read()
        if "jupyter_displays_for_obsidian" in existing_hook:
            raise ValueError("The hook is already set up for jupyter_displays_for_obsidian")
        with open(hook_path, "a") as f:
            # Find the line with the exit command
            lines = existing_hook.split("\n")
            for i, line in enumerate(lines):
                if line.startswith("exit"):
                    break
            # Add the hook content before the exit command
            lines.insert(i, hook_content)
            f.write("\n".join(lines))
    else:
        # Create the hook
        with open(hook_path, "w") as f:
            # Add the first line
            f.write("#!/bin/sh\n")
            # Add the hook content
            f.write(hook_content)
            # Add the exit command
            f.write("\nexit 0\n")
        os.chmod(hook_path, 0o755)


def setup_git_ignore_md(path: str):
    """
    Function to add .md files to .gitignore (except README.md)
    :param path: str: path to the folder to set up the git ignore
    :return:
    """
    # Check if the path is a directory
    if not os.path.isdir(path):
        raise ValueError("path should lead to a folder")
    # Check if the path is a git repository
    if not os.path.isdir(os.path.join(path, ".git")):
        raise ValueError("path should lead to a git repository")

    # Check if the .gitignore file exists
    if not os.path.isfile(os.path.join(path, ".gitignore")):
        # Create the .gitignore file
        with open(os.path.join(path, ".gitignore"), "w") as f:
            f.write("*.md\n")
            f.write("!README.md\n")
    else:
        # Add the .md files to the .gitignore
        with open(os.path.join(path, ".gitignore"), "a") as f:
            f.write("*.md\n")
            f.write("!README.md\n")

def setup_git_ignore_assets(path: str):
    """
    Function to add assets folder to .gitignore
    :param path: str: path to the folder to set up the git ignore
    :return:
    """
    # Check if the path is a directory
    if not os.path.isdir(path):
        raise ValueError("path should lead to a folder")
    # Check if the path is a git repository
    if not os.path.isdir(os.path.join(path, ".git")):
        raise ValueError("path should lead to a git repository")

    # Check if the .gitignore file exists
    if not os.path.isfile(os.path.join(path, ".gitignore")):
        # Create the .gitignore file
        with open(os.path.join(path, ".gitignore"), "w") as f:
            f.write("assets/\n")
    else:
        # Add the assets folder to the .gitignore
        with open(os.path.join(path, ".gitignore"), "a") as f:
            f.write("assets/\n")


def main_cli():
    fire.Fire(main)
