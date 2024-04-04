import re

from ..view.view_utils import pick_view, view, get_supported_display_types


def format_markdown(markdown: str,
                    notebook_path: str,
                    ) -> str:
    """
    Function to format the markdown string.
    :param markdown: str: the markdown string to format
    :param notebook_path: str: the name of the notebook
    :return: str: the formatted markdown string
    """

    # Replace '```python' with '```run-python'
    markdown = re.sub(r'```python', '```run-python', markdown)

    # Remove lines starting with ![png]
    markdown = re.sub(r'^!\[png\].*$', '', markdown, flags=re.MULTILINE)

    # Process the markdown
    lines = markdown.split('\n')
    processed_lines = []
    display_queue = []
    # Get the list of supported display types
    supported_display_types = get_supported_display_types()
    display_counter = {display_type: 0 for display_type in supported_display_types}

    in_code_block = False
    for i, line in enumerate(lines):

        # Identify if we are in a code block
        if line.startswith('```run-python'):
            in_code_block = True
            processed_lines.append(line)

        elif line.startswith('```'):
            in_code_block = False
            # Add the line to the processed lines
            processed_lines.append(line)
            # Add the display queue to the processed lines
            if display_queue:
                processed_lines.append('\n#### Results')
            processed_lines.extend(display_queue)
            # Add a newline for readability
            processed_lines.append('')
            # Clear the display queue
            display_queue = []

        else:
            # Check if we are in a code block
            if in_code_block:
                # Check if the line contains a display
                which_view = pick_view(line)
                processed_lines.append(line)
                if which_view is not None:
                    view(which_view, line, display_queue, display_counter, notebook_path)
            # else:
                # Don't Add the line to the processed lines
                # processed_lines.append(line)

    # Join the processed lines
    processed_markdown = '\n'.join(processed_lines)

    return processed_markdown
