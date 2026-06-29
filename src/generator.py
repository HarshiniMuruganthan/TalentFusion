"""
generator.py

Generates the final candidate JSON file.
"""

import json
import os


class Generator:

    def generate(self, candidate):

        # Create output folder if it doesn't exist
        os.makedirs("output", exist_ok=True)

        output_file = "output/result.json"

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(candidate, file, indent=4)

        return output_file