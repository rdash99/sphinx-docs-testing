# sphinx-docs-testing
 
In order for the action to build the documentation, you need to create a /docs folder in your repository and add a sphinx project in it. Copy the contents of the folder in this repository to your repository and modify the conf.py.

All custom pages should be added to the /docs folder. The index.rst file in the /docs folder should be modified to include the custom pages. You can find an example of an index.rst file in this repository.

Once you have created the sphinx project, you need to configure it by editing the conf.py file. You can find an example of a conf.py file in this repository.

The sections that you need to edit are:

- `Line 18`: set the path to the root of each of your packages/modules (e.g. `../src`)


- `extensions`: add the `sphinx.ext.autodoc` extension
- `extensions`: add the `sphinx.ext.autosummary` extension
- `extensions`: add the `autoapi.extension` extension
- `extensions`: add the `"sphinx_markdown_builder"` extension

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



Finally, you need to create a workflow file in your repository. You can copy the contents of the workflow file in this repository to your repository. The workflow file is located in `.github/workflows/sphinxBuild.yml`.

Change the `on` section to specify when you want the action to run from the current setup to something sensible. You can find more information about the `on` section [here](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#on).

You will need to provide the following information:

A github token with at least the `repo` scope. You can create a new token by going to your github settings, then Developer settings, then Personal access tokens. Make sure to copy the token as you will not be able to see it again. Add this as the GH_TOKEN secret in your repository.

Replace the `REPO` environment variable with the name of your wiki repository.

All the environment variable options can be found [here](https://github.com/s0/git-publish-subdir-action#configuration)
