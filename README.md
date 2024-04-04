# Obsidianize

A simple package to convert Jupyter notebooks to markdown files that can be easily used and embeded in Obsidian.

Proper formating and Obsidian usability of the Python cells relies on the [Execute code](https://github.com/twibiral/obsidian-execute-code) plugin for obsidian,
as well as a trust in the user to use the functions from the package to display the assets in the notebook itself.
These functions serve both as a placeholder for parsing, as well as a way to export the assets in the notebook to the markdown file, so that they can be displayed in Obsidian.

## Installation

Pull the package from GitHub:

```bash
git pull github.com/AdrienBolling/Obsidianize
```

Then install it with pip:

```bash
pip install .
```

## Usage

There are two main functions in the package:

```bash
obsidianize <git_repository_path>
```
to set up a git repository to automatically convert notebooks to markdown files when they appear in a commit.
(This behaviour relies on adding a pre-commit hook to the repository. The hook will automatically convert the notebooks to markdown files before each commit.)

and
```bash
obsidianize <notebook_path / path_that_contains_notebooks>
```
to convert a single notebook or all notebooks in a folder to markdown files.


You can also call
```bash
obsidianize refresh <git_repository_path>
```
to manually refresh the markdown files in the repository without performing a commit.


## Example

### Notebook conversion

To convert all notebooks in a folder to markdown files, you can use the following command:

```bash
obsidianize /path/to/folder
```

To set up a git repository to automatically convert notebooks to markdown files when they appear in a commit, you can use the following command:

```bash
obsidianize /path/to/git/repository
```

### Notebook content

The package will handle the exporting of the assets if you use its function in your notebook.
These functions are for now :
```python
from obsidianize import obsidian_pyplot, obsidian_plotly, obsidian_pandas

obsidian_pyplot(figure, title)
obsidian_plotly(figure, title)
obsidian_pandas(dataframe, title)
```

As their name suggests, they are respectively for matplotlib, plotly and pandas assets.
The title is not optional for now, you have to give your figure or dataframe a title to be able to export it.

These functions will replace the usual display functions in your notebook, and will also export the assets in the markdown file.

For example, instead of using
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.title("Simple plot")
plt.show()
```
you should use
```python
import matplotlib.pyplot as plt
from obsidianize import obsidian_pyplot

fig = plt.figure()
plt.plot([1, 2, 3, 4])
obsidian_pyplot(fig, "Simple plot")
```
(Similarly for plotly and pandas, replacing the usual display functions with the obsidianize ones.)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Concerns

- Please note that these won't be compatible with plt.show() or fig.show() or df which have been placed in a loop.
However, you shouldn't be doing that anyway, as it is not a good practice to display multiple figures in a loop in a notebook, use subplots instead.

- Due to the issue of getting the name of a notebook while it is being executed, this package has been designed to be 
compatible with use for Jupyter, JupyterLab, DataSpell, Pycharm, and VSCode.

## Additional information
Converting a notebook won't execute the code cells. To do so, you can either execute the notebook by yourself, 
which will export the assets if you used the package properly, or do it later in Obsidian thanks to Execute Code by 
running the cells.

## Reporting issues
This package is still under development, and there might be some issues with the conversion of the notebooks.
Please report any issues you encounter on the [GitHub repository](githum.com/AdrienBolling/Obsidianize) or on 
[Discord](https://discord.gg/FDsCDgnrQ8). As this is my first proper project feel free to give me any feedback on the code or the package itself.
