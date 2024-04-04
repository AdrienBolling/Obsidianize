import os
from pathlib import Path

from obsidianize.src.utils.path_utils import get_assets_path, get_vault_root
from obsidianize.src.utils.sanitize import get_figure_title


def view_pyplot(
        line: str,
        display_queue: list,
        display_counter: dict,
        notebook_path: str,
):
    """
    Function to process a pyplot figure.
    :param line: str: the line to process
    :param display_queue: list: the list of displays
    :param display_counter: dict: the list of figure counters
    :param notebook_path: str: the name of the notebook
    :return: nothing
    """

    # Get the figure title
    figure_title = get_figure_title(line)

    # If the figure title is None, set it to the figure counter
    if figure_title is None:
        figure_title = f"pyplot_{display_counter['pyplot']}"

    # Get the assets folder for this notebook, from the obsidian vault
    assets_folder = get_assets_path(notebook_path)
    obsidian_vault_path = get_vault_root(notebook_path)
    assets_folder = Path(assets_folder).relative_to(obsidian_vault_path)

    # Create the line to embed the figure in the markdown
    display_queue.append(f"![{figure_title}]({os.path.join(assets_folder, figure_title)}.png)")

    # Increment the figure counter
    display_counter['pyplot'] += 1

