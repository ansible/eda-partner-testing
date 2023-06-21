# EDA Partner Testing Templates
This repository is equipped with testing templates and details
for Partners who develop EDA content for the Certified Content
and Validated Content programs. 

These templates are intended to be used for local and CI testing
with the Python testing tool, `tox`. 

## What is Tox?

`tox` is a virtual environment management and testing CLI tool used
for testing Python files in configurable environments. It provides
a simple format for running a variety of linters and static analysis
tests, all in segmented environments. 

For more information about `tox`, visit their wiki at:
[https://tox.wiki/en/latest/](https://tox.wiki/en/latest/)

`tox` will install all required tooling and dependencies of that tooling. 

## Required Tests for Certified/Validated EDA Content

To be certified or validated, collections containing EDA plugin content
must pass the following linters:

- `ruff` : [ruff docs](https://beta.ruff.rs/docs/)
- `darglint` : [darglint on pypi](https://pypi.org/project/darglint/) 
- `pylint` : [pylint docs](https://pylint.readthedocs.io/en/latest/)

These linters are subject to change or have additional requirements added
over time, at the suggestion of the Ansible Partner Engineering team and
the Event-Driven Ansible team. 

**Note:** For EDA rulebooks, `ansible-lint` will be run over rulebooks for
structural enforcement. That is not covered in these templates. `ansible-lint`
docs can be found at [Ansible Lint readthedocs](https://ansible-lint.readthedocs.io/)

## Included Templates

### `tox.ini`

The `tox.ini` `tox` template is designed to run over the whole project's file structure. 

### Github Workflow for `tox`

The included workflow at `.github/workflows/linters.yml` can be copied into the `.github/workflows/` dir in the collection root. 

## Collection structure

This will result in a collection with the following structure:

    .                           # Collection root
    ├── .github
    │   ├── workflows
    │   └── ├── linters.yml     # Insert the linters.yml workflow template here
    │       └── ...             # Additional workflows (if applicable)  
    ├── extensions              # Extensions dir
    │   └── eda                 # EDA dir (contains all EDA content - `rulebooks/` and `plugins/`)
    │       ├── rulebooks           
    │       │   └── *.yml...        
    │       └── plugins             
    │           ├── event_filter
    │           │   └── *.py
    │           └── event_source
    │               └── *.py
    ├── meta
    │   ├── runtime.yml
    │   └── ...
    ├── tests
    │   └── ...
    ├── galaxy.yml
    ├── README.md
    ├── CHANGELOG.rst           # or `.md`, and/or have a `changelogs/changelog.yml` file
    │   tox.ini                 # Insert the tox.ini template here
    │   test_requirements.txt   # Insert the test_requirements.txt testing dependencies here          
    └── ...                     # Other collection content (`plugins/`, `roles/`, etc.)

## Requirements

To use the `tox.ini` template in your dev environment, `tox` must be locally installed,
please refer to the Github actions `linters.yml` workflow. 

To install `tox`, run:

    python3 -m pip install tox

The linters used in the `tox.ini` file will be automatically installed when each testenv is called.

## Running `tox` Locally

To run `tox` in your local dev environment, run the following command from the project's root folder:

```
tox -e linters  # To run the tox main environment that will run all the lint checks.
```

## Running `tox` in CI

Depending on the CI tooling the user has, the only main requirement is to have `tox` installed, as a
reference check `.github/workflows/tox.yml`

In the particular case of using Github actions, place the `.github/workflows/linters.yml`, `tox.ini`,
and `test_requirements.txt` files into the collection repository's preserving the relative path
to the collection. 

Make sure Github Actions is enabled on the repository. 

The workflow should run automatically on new PRs and push actions. 

## Add to the `build_ignore` list

Add the `.github/` directory to the `build_ignore` list in the collection's `galaxy.yml` file to prevent the dir from being included in the collection tarball. 

## Questions?

If you have questions about these templates, please reach out to **ansiblepartners@redhat.com** to contact the Ansible Partner Engineering team. 
