"""
This file contains the utils functions used in the view module of the obsidianize package.
"""
from pathlib import Path
from .pyplot import view_pyplot
from .pandas import view_pandas
from .plotly import view_plotly


def get_supported_display_types() -> list:
    """
    Function to get the list of supported display types.
    :return: list: the list of supported display types
    """
    view_folder_path = Path(__file__).parent
    view_files = view_folder_path.glob('*.py')
    # Remove the __init__.py file and the view_utils.py file
    view_files = [file for file in view_files if file.stem != '__init__' and file.stem != 'view_utils']
    # Get the list of supported display types
    supported_display_types = [file.stem for file in view_files]
    return supported_display_types


def pick_view(
        line: str,
):
    """
    Function to determine which view function to call.
    :return: str: the name of the view function to call (or None if no view placeholder is found)
    """
    # Get the list of supported display types
    supported_display_types = get_supported_display_types()
    # Check if the line contains a display type
    for display_type in supported_display_types:
        if f"obsidian_{display_type}(" in line:
            return display_type
    return None


def view(
        which_view: str,
        line: str,
        display_queue: list,
        display_counter: dict,
        notebook_path: str,
):
    """
    Function to call the appropriate view function.
    :param which_view: str: the name of the view function to call
    :param line: str: the line to process
    :param display_queue: list: the list of displays
    :param display_counter: dict: the list of figure counters
    :param notebook_path: str: the name of the notebook
    :return: nothing
    """

    # Get the view function
    view_function = globals()["view_" + which_view]
    # Call the view function
    view_function(line=line, display_queue=display_queue, display_counter=display_counter, notebook_path=notebook_path)
