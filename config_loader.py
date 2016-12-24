"""
Generate the config settings.

Responsible for checking that the settings are correct.
Get returns the config to be used.
"""

default_config = {
    "Question Random Order": True,
    "Answer Random Order": True,
    "Default Answer Selection Count": 4,
    "Total Questions": 10,
    "Wrong Answers per Question": 10,
    }

def get():
    config = default_config.copy()
    return config