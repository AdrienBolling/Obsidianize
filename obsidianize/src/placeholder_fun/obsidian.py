import os

import matplotlib
import numpy as np
import pandas as pd
import plotly
from matplotlib import pyplot as plt

from obsidianize.src.utils.path_utils import get_notebook_path, get_assets_path, in_obsidian_env
from obsidianize.src.utils.sanitize import sanitize_name
from IPython.display import display


def obsidian_pyplot(
        figure: matplotlib.figure.Figure,
        title: str,
        path_to_notebook: str = None,
):
    """
    Function to display a pyplot figure in Obsidian. Replace your usual `plt.show()` with this function to display
    figures in Obsidian. This function is used as a way to parse the show() method of pyplot figures as well as the
    title of the figure.
    :param figure: str: the pyplot figure to display
    :param title: str: the title of the figure
    :param path_to_notebook: str: the path to the notebook, this argument is optional as long as you're using Jupyter
    / JupyterLab / VSCode / Jetbrains IDEs
    :return: None
    """
    # Check if there is a figure
    if figure is None:
        raise ValueError("Please provide a figure to display")
    # Check if the title is None
    if title is None:
        raise ValueError("Please provide a title for the figure")
    # Check if the path to the notebook is None
    if path_to_notebook is None:
        path_to_notebook = get_notebook_path()

    # Get the corresponding assets folder
    assets_folder = get_assets_path(path_to_notebook)
    print(assets_folder)
    # Get the figure title
    figure_title = sanitize_name(title)

    # If the figure title is None, go to the assets folder to figure out the display counter for this type of figure
    if figure_title is None:
        counter = 0
        # Check for all the files in the assets folder
        for file in os.listdir(assets_folder):
            # If the file is a pyplot figure, increment the counter
            if "pyplot" in file:
                counter += 1
        # Set the figure title to the counter
        figure_title = f"pyplot'_{counter}"

    # Get the figure number
    figure_number = figure.number
    # Plot the figure
    plt.figure(figure_number)
    # Set the title of the figure
    plt.title(title)

    # Check if we're in the obsidian code execution environment
    if not in_obsidian_env():
        plt.show(figure)
    # In all cases, save the figure
    figure.savefig(os.path.join(assets_folder, f"{figure_title}.png"))


def obsidian_pandas(
        df: pd.DataFrame,
        title: str,
        path_to_notebook: str = None,
        format: str = "markdown"

):
    """
    Function to display a pandas dataframe in Obsidian. Replace your usual `print(df)` with this function to display
    dataframes in Obsidian. This function is used as a way to parse the print() method of pandas dataframes as well as
    the title of the dataframe.
    :param df: pd.DataFrame: the pandas dataframe to display
    :param title: str: the title of the dataframe
    :param path_to_notebook: str: the path to the notebook, this argument is optional as long as you're using Jupyter
    / JupyterLab / VSCode / Jetbrains IDEs
    :param format: str: the format to display the dataframe in (either "markdown" or "latex") ("latex" is broken for
    display in obsidian, either way the dataframe is saved in a .tex file)
    :return: None
    """
    # Check if there is a dataframe
    if df is None:
        raise ValueError("Please provide a dataframe to display")
    # Check if the title is None
    if title is None:
        raise ValueError("Please provide a title for the dataframe")
    # Check if the path to the notebook is None
    if path_to_notebook is None:
        path_to_notebook = get_notebook_path()

    # Get the corresponding assets folder
    assets_folder = get_assets_path(path_to_notebook)

    # Get the dataframe title
    dataframe_title = sanitize_name(title)

    if dataframe_title is None:
        # If the dataframe title is None, go to the assets folder to figure out the display counter for this type of
        # figure
        counter = 0
        # Check for all the files in the assets folder
        for file in os.listdir(assets_folder):
            # If the file is a pandas dataframe, increment the counter
            if "pandas" in file:
                counter += 1
        # Set the dataframe title to the counter
        dataframe_title = f"pandas_{counter}"

    # Check if we're in the obsidian code execution environment
    if not in_obsidian_env():
        # Set the title of the dataframe
        print(title)
        # Display the dataframe
        display(df)

    # In all cases, save the dataframe
    # We are saving it to a Latex formating for better display in Obsidian
    print(os.path.join(assets_folder, f"{dataframe_title}.tex"))
    # df.to_latex(os.path.join(assets_folder, f"{dataframe_title}.tex"), caption=title, label=title)
    df.to_markdown(os.path.join(assets_folder, f"{dataframe_title}.md"))


def obsidian_plotly(
        fig: plotly.graph_objs.Figure,
        title: str,
        path_to_notebook: str = None,
        svg: bool = True,
        html: bool = True,
):
    """
    Function to display a plotly figure in Obsidian. Replace your usual `fig.show()` with this function to display
    figures in Obsidian. This function is used as a way to parse the show() method of plotly figures as well as the
    title of the figure.
    This will save the figure as an asset, by default in 3 formats (png for embedding, svg for article writing, html for interactivity)
    :param fig: str: the plotly figure to display
    :param title: str: the title of the figure
    :param path_to_notebook: str: the path to the notebook, this argument is optional as long as you're using Jupyter
    / JupyterLab / VSCode / Jetbrains IDEs
    :param svg: bool: whether to save the figure in svg format (by default True)
    :param html: bool: whether to save the figure in html format (by default True)
    :return: None
    """
    # Check if there is a figure
    if fig is None:
        raise ValueError("Please provide a figure to display")
    # Check if the title is None
    if title is None:
        raise ValueError("Please provide a title for the figure")
    # Check if the path to the notebook is None
    if path_to_notebook is None:
        path_to_notebook = get_notebook_path()

    # Get the corresponding assets folder
    assets_folder = get_assets_path(path_to_notebook)

    # Get the figure title
    figure_title = sanitize_name(title)

    # If the figure title is None, go to the assets folder to figure out the display counter for this type of figure
    if figure_title is None:
        counter = 0
        # Check for all the files in the assets folder
        for file in os.listdir(assets_folder):
            # If the file is a plotly figure, increment the counter
            if "plotly" in file:
                counter += 1
        # Set the figure title to the counter
        figure_title = f"plotly'_{counter}"

    # Check if we're in the obsidian code execution environment
    if not in_obsidian_env():
        # Set the title of the figure
        print(title)
        # Display the figure
        fig.show()

    # In all cases, save the figure
    if svg:
        fig.write_image(os.path.join(assets_folder, f"{figure_title}.svg"))
    if html:
        fig.write_html(os.path.join(assets_folder, f"{figure_title}.html"), auto_open=False)
    fig.write_image(os.path.join(assets_folder, f"{figure_title}.png"))
