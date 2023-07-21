# sphinx-docs-testing
 
In order for the action to build the documentation, you need to create a /docs folder in your repository and add a sphinx project in it. You can use the sphinx-quickstart command to create a new sphinx project. Alternatively, you can copy the contents of the folder in this repository to your repository and modify the conf.py.

Once you have created the sphinx project, you need to configure it by editing the conf.py file. You can find an example of a conf.py file in this repository.

The sections that you need to edit are:

- `Line 18`: set the path to the root of each of your packages/modules (e.g. `../src`)


- `extensions`: add the `sphinx.ext.autodoc` extension
- `extensions`: add the `sphinx.ext.autosummary` extension
- `extensions`: add the `autoapi.extension` extension

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "autoapi.extension",
]
```

- `project`: set the name of your project
- `copyright`: set the copyright
- `author`: set the author of your project

- `autoapi_dirs`: set the path/s to the directory/s that contains the source code of your project
- `autoapi_ignore`: set the path/s to the directory/s that contains code that you want to ignore, such as tests

optionally, you can also set the following:
`html_theme`: set the theme of your documentation (e.g. `sphinx_rtd_theme`)



Finally, you need to create a workflow file in your repository. You can find an example of a workflow file in this repository. The workflow file should be located in the .github/workflows folder of your repository.
