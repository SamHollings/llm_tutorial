# LLM Tutorial

This repo contains notebooks which walk you through some simple LLM implementations. It uses free software and can all be run inside google collab, for maximum accessibility.

## Contact

This repo is currently maintained by @samhollings - raise and issue or a pull request if you have any suggestions (or just contact me directly!)

## Description

This repo contains guides on:
- [**RAG (Retreival Augemented Generation)**](llm_tutorial_rag.ipynb)<a target="_blank" href="https://colab.research.google.com/github/SamHollings/llm_tutorial/blob/main/llm_tutorial_rag.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>: an LLM which looks things up in a database before responding - a cheap and easy way of make it seem like an LLM has local knowledge
- [**RAG with sources**](llm_tutorial_rag_sources.ipynb)<a target="_blank" href="https://colab.research.google.com/github/SamHollings/llm_tutorial/blob/main/llm_tutorial_rag_sources.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> : shows you how get the LLM to give sources for it's claims, and generally how to have more control over the prompts used in the pipeline.
- [**Open Source LLM using Llama2 **](llm_tutorial_llama2.ipynb)<a target="_blank" href="https://colab.research.google.com/github/SamHollings/llm_tutorial/blob/main/llm_tutorial_llama2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> (author: [Adam Hollings](https://github.com/AdamHollings) : Show you how to create your own llm chatbot using the open source llama2 model. No api token required!
- more coming soon...

## Prerequisites

- knowledge-wise, some ability with python. Knowledge of data science would be useful, but not crucial (at least at the start). Interest in LLMs will help!
- system-wise: the requirements can be found in the [`requirements.txt`](requirements.txt) file, and can be loaded `pip`.

## Getting Started
### Google Colab
Open one of the google colab links above!

### Clone the repo

Clone the repository. To learn about what this means, and how to use Git, see the [Git guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/git/using-git-collaboratively/).

```
git clone <insert URL>
```

### install dependencies

Make a [virtual environment](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/virtual-environments/venv/) and install the dependencies:
```
pip install -r requirements.txt
```

## Project structure


```text
|   .env_example                      <- Copy this, rename to ".env" and fill in with your keys. It's used to store access tokens.
|   .gitignore                        <- Files (& file types) automatically removed from version control for security purposes
|   config.toml                       <- Configuration file with parameters we want to be able to change (e.g. date)
|   llm_tutorial_rag_sources.ipynb    <- a tutorial for how do get a RAG LLM to give citations for its claims
|   llm_tutorial_rag.ipynb            <- a basic tutorial introducing RAG
|   requirements.txt                  <- The list of python libraries we've used, used by pip to install them.
|   pyproject.toml                    <- Configuration file containing package build information
|   LICENCE                           <- License info for public distribution
|   README.md                         <- Quick start guide / explanation of your project
|   
|
+---src                               <- Scripts with functions for use in 'create_publication.py'. Contains project's codebase.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---utils                         <- Scripts relating to configuration and handling data connections e.g. importing data, writing 
|   |                                    to a database etc.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |       logging_config.py         <- Configures logging
|   |
|   +---processing                    <- [currently not used] Scripts with modules containing functions to process data i.e. clean and derive new fields
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---data_ingestion                <- [currently not used] Scripts with modules containing functions to preprocess read data i.e. perform validationdata quality checks, other preprocessing etc.
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---data_exports
|   |       __init__.py               <- [currently not used] Makes the functions folder an importable Python module
|
|
+---tests
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---backtests                     <- Comparison tests for the old and new pipeline's outputs
|   |       backtesting_params.py
|   |       test_compare_outputs.py
|   |       __init__.py               <- Makes the functions folder an importable Python module
|   |
|   +---unittests                     <- Tests for the functional outputs of Python code
|   |       test_data_connections.py
|   |       test_processing.py
|   |       __init__.py               <- Makes the functions folder an importable Python module
```

### `root`

In the highest level of this repository (known as the 'root'), there is one Python file: `create_publication.py`. This top level file should be the main place where users interact with the code, where you store the steps to create your publication.

This file currently runs a set of example steps using example data.

### `src`

This directory contains the meaty parts of the code. By organising the code into logical sections, we make it easier to understand, maintain and test. Moreover, tucking the complex code out of the way means that users don't need to understand everything about the code all at once.

* `data_connections.py` handles reading data in and writing data back out.
* `processing` folder contains the core business logic.
* `utils` folder contains useful reusable functions (e.g. to set up logging, and importing configuration settings from `config.toml`)
* `write_excel.py` contains functions relating to the final part of the pipeline, any exporting or templating happens here. This is a simplistic application of writing output code to an Excel spreadsheet template (.xlsx). A good example of this application is: [NHS sickness absence rates publication](https://github.com/NHSDigital/absence-rates). We highly recommend to use [Automated Excel Production](https://nhsd-git.digital.nhs.uk/data-services/analytics-service/iuod/automated-excel-publications) for a more in depth Excel template production application.

## Adapting for your project

Just take whatever code you need, and reimplement it. This was made mostly in the form of Jupyter notebooks for ease of use and demos, however I wouldn't recommend that for most applications - but it can be very useful when getting started and playing with the code.

## Licence

> The [LICENCE](/LICENCE) file will need to be updated with the correct year and owner

Unless stated otherwise, the codebase is released under the MIT License. This covers both the codebase and any sample code in the documentation.
