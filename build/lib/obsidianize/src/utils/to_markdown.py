# Import the markdown exporter
from nbconvert import MarkdownExporter


def convert_to_markdown(notebook):
    """
    Function to convert a jupyter notebook to a markdown string.
    :param notebook: notebook: the notebook to convert
    :return: str: the markdown string
    """

    # Create the markdown exporter
    exporter = MarkdownExporter()

    # Convert the notebook to markdown
    markdown, _ = exporter.from_notebook_node(notebook)

    return markdown
