# EDA Partner Testing Templates
This repository is equipped with testing templates and details for Partners who develop EDA content for the Certified Content and Validated Content programs. 

These templates are intended to be used for local and CI testing with the Python testing tool, `tox`. 

## What is Tox?

`tox` is a virtual environment management and testing CLI tool used for testing Python files in configurable environments. It provides a simple format for running a variety of linters and static analysis tests, all in segmented environments. 

For more information about `tox`, visit their wiki at: [https://tox.wiki/en/latest/](https://tox.wiki/en/latest/)

`tox` will install all required tooling and dependencies of that tooling. 

## Required Tests for Certified/Validated EDA Content

To be certified, collections containing EDA content must pass the following linters:

- `ruff` : [ruff docs](https://beta.ruff.rs/docs/)
- `darglint` : [darglint on pypi](https://pypi.org/project/darglint/) 
- `pylint` : [pylint docs](https://pylint.readthedocs.io/en/latest/)

These linters are subject to change or have additional requirements added over time, at the suggestion of the Ansible Partner Engineering team and the Event-Driven Ansible team. 


## Included Templates

### `tox.ini`

The `tox.ini` template is designed to run over the `<collection_root>/extensions/eda/plugins` directory and included content. 

**IMPORTANT NOTE:** If the collection does not have an `<collection_root>/extensions/eda/plugins/event_source` or `<collection_root>/extensions/eda/plugins/event_filter` dir, remove or comment out the corresponding `pylint` environment from the `tox.ini` file. This would be the `[testenv:pylint-event-source]` section or `[testenv:pylint-event-filter]` section in the `tox.ini` file. 

### Github Workflow for `tox`

The included workflow at `.github/workflows/tox.yml` can be copied into a collection repo in the following structure:

    .                           # Collection root
    ├── .github
    │   ├── workflows
    │   └── ├── tox.yml         # Insert tox template here
    │       └── ...             # Additional workflows (if applicable)  
    ├── extensions              # Extensions dir
    │   ├── eda                 # EDA dir (contains all EDA content - `rulebooks/` and `plugins/`)
    │       ├── rulebooks           
    │       │   └── *.yml...        
    │       └── plugins             
    │           ├── event_filter
    │           │   └── *.py
    │           └── event_source
    │               └── *.py
    │           
    ├── meta
    │   ├── runtime.yml
    │   └── ...
    ├── tests
    │   └── ...
    ├── galaxy.yml
    ├── README.md
    ├── CHANGELOG.rst           # or `.md`, and/or have a `changelogs/changelog.yml` file
    ├── tox.ini                 # `tox.ini` MUST be in the collection root to work with the included workflow            
    └── ...                     # Other collection content (`plugins/`, `roles/`, etc.)

## Requirements

To use the `tox.ini` template in your dev environment, `tox` must be locally installed. 

To install `tox`, run:

    pip install tox

The linters used in the `tox.ini` file will be automatically installed when each testenv is called. 

## Running `tox` Locally

To run `tox` in your local dev environment with this template, you must run tox from the dir above your collection root. This is because of a `setuptools` error that will not allow tox to run in a "flat-hierarchy" environment. 

Our recommendation is to keep a **copy** of the `tox.ini` file one dir above the collection root in your local environment, and when locally testing, run `tox` from the dir above your collection:

    .                               # One dir above the collection
    ├── tox.ini
    ├── <collection_dir>            # Local collection dir
    │   └── <collection_content> ...
    └── ...

To run tox with this template, first be **in** the directory above the collection, then run:

    tox -- <collection_dir>

The `--` flag tells `tox` to pass the next argument into the `tox.ini` file where `{posargs}` is specified. 

This is how the template will find the EDA plugin content inside your collection. Changing this or not adhering to this structure could cause `tox` to give a false clean result, which is why we recommend sticking to this structure. 


## Running `tox` in CI

Place the `.github/workflows/tox.yml` file into the collection repository's `.github/workflows` dir. 

Make sure Github Actions is enabled on the repository. 

The workflow should run automatically on new PRs and push actions. 


## Common Errors

If you receive a `setuptools` error, you will need to adjust the location of the tox file within the workflow job to be one directory above the collection, as specified above.

Make sure that the `pylint` paths inside the file point directly to the `*.py` files inside `<root>/extensions/eda/plugins/event_source/*.py` and `<root>/extensions/eda/plugins/event_filters/*.py` paths, to avoid errors about missing `__init__.py` files. 


## Questions?

If you have questions about these templates, please reach out to **ansiblepartners@redhat.com** to contact the Ansible Partner Engineering team. 

