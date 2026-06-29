"""
config_loader.py

Loads configuration settings.
"""

import json


class ConfigLoader:

    def load(self):

        with open("config/default.json", "r") as file:

            config = json.load(file)

        return config