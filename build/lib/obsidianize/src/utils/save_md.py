import os


def save_markdown(markdown: str, path: str):
    """
    Function to save a markdown string to a file.
    :param markdown:
    :param path:
    :return:
    """

    md_path = path.replace('.ipynb', '.md')
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown)

    print(f"Notebook {os.path.basename(path)} has been processed and saved to {md_path}.")
