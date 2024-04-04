import re


def sanitize_name(name):
    """Sanitize names to contain only Latin letters, numbers, and dashes."""
    return re.sub(r'[^a-zA-Z0-9-]', '', name.replace(' ', '-').replace('_', '-'))


def get_figure_title(
        line: str,
):
    """
    Function to get the figure title from the line.
    :param line: str: the line to process
    :return: str: the figure title
    """
    # Get the args of the obsidian_"generic" function (use a wildcard for the generic)
    args = line.split("obsidian_")[1].split("(")[1].split(")")[0]
    # Check if there are multiple args
    if ", " in args:
        # Get the figure title
        figure_title = args.split(", ")[1]
        # Get the figure title, with the eventuality that the user put "title='figure_title'" or
        # "title="figure_title"", or just "figure_title"
        figure_title = figure_title.split("=")
        # Check if the title is in the first or second position
        if len(figure_title) == 1:
            figure_title = figure_title[0]
        else:
            figure_title = figure_title[1]
        # Remove the quotes around the title if there are any
        figure_title = figure_title.replace("'", "").replace('"', "")
        # Sanitize the figure title
        figure_title = sanitize_name(figure_title)

    else:
        # Give a None title
        figure_title = None
    return figure_title
