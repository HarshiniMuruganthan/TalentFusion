"""
audit.py

Enterprise Audit Trail

Logs every pipeline operation.
"""

import json
import os
from datetime import datetime


class Audit:

    def __init__(self):

        self.logs = []

    def log(self, module, action, details=""):

        self.logs.append({

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "module": module,

            "action": action,

            "details": details

        })

    def save(self, path="output/audit_log.json"):

        os.makedirs("output", exist_ok=True)

        with open(path, "w") as file:

            json.dump(self.logs, file, indent=4)

        return path