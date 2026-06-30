"""
resolver.py

Conflict Resolution Engine
"""


class Resolver:

    def __init__(self):

        self.priority = {
            "Resume": 1,
            "Recruiter CSV": 2
        }

    def resolve(self, candidate, csv_data):

        conflicts = []

        fields = [
            "name",
            "email",
            "phone",
            "company",
            "designation",
            "location"
        ]

        for field in fields:

            resume_value = candidate.get(field)
            csv_value = csv_data.get(field.capitalize())

            if csv_value is None:
                continue

            if resume_value is None:
                continue

            resume_value = str(resume_value).strip()
            csv_value = str(csv_value).strip()

            if resume_value != csv_value:

                candidate[field] = csv_value

                conflicts.append({
                    "field": field,
                    "resume_value": resume_value,
                    "csv_value": csv_value,
                    "selected_value": csv_value,
                    "winner": "Recruiter CSV",
                    "reason": "Recruiter CSV has higher priority"
                })

        candidate["conflicts"] = conflicts

        return candidate