import os
from pathlib import Path

from jupyter_to_obsidian.src.utils.path_utils import get_assets_path, get_vault_root
from jupyter_to_obsidian.src.utils.sanitize import get_figure_title


def view_pandas(
        line: str,
        display_queue: list,
        display_counter: dict,
        notebook_path: str,
):
    """
    Function to process a pandas DataFrame.
    :param line: str: the line to process
    :param display_queue: list: the list of displays
    :param display_counter: dict: the list of figure counters
    :param notebook_path: str: the path of the notebook
    :param path: str: the path to the notebook
    :return: nothing
    """

    # Get the figure title
    figure_title = get_figure_title(line)

    # If the figure title is None, set it to the figure counter
    if figure_title is None:
        figure_title = f"pandas_{display_counter['pandas']}"

    # Get the assets folder for this notebook
    assets_folder = get_assets_path(notebook_path)

    # Copy the content of the pandas DataFrame formated as a markdonw table in a file and embed it in the markdown
    assets_folder = get_assets_path(notebook_path)
    obsidian_vault_path = get_vault_root(notebook_path)
    assets_folder = Path(assets_folder).relative_to(obsidian_vault_path)
    display_queue.append(f"![{figure_title}]({os.path.join(assets_folder, figure_title)}.md)")
    display_queue.append("\n")

    # Increment the figure counter
    display_counter['pandas'] += 1
