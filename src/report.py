"""
report.py

Generates a transformation report for the pipeline.
"""

import json
import os
import time
from datetime import datetime


class Report:

    def generate(self, candidate, start_time):

        end_time = time.time()

        execution_time = round(end_time - start_time, 3)

        report = {

            "pipeline_status": "Completed",

            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "execution_time_seconds": execution_time,

            "sources_processed": 2,

            "records_processed": 1,

            "fields_extracted": len([
                k for k in [
                    "name",
                    "email",
                    "phone",
                    "location",
                    "skills",
                    "education",
                    "experience"
                ]
                if candidate.get(k)
            ]),

            "fields_merged": len([
                k for k in [
                    "name",
                    "email",
                    "phone",
                    "location",
                    "skills",
                    "education",
                    "experience",
                    "company",
                    "designation"
                ]
                if candidate.get(k)
            ]),

            "overall_confidence": candidate.get(
                "overall_confidence", 0
            ),

            "profile_completion": candidate.get(
                "profile_health", {}
            ).get("completion", 0),

            "validation_status": candidate.get(
                "validation", {}
            ).get("is_valid", False)
        }

        os.makedirs("output", exist_ok=True)

        report_path = "output/transformation_report.json"

        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        return report_path