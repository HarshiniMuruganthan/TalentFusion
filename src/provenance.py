"""
provenance.py

Tracks where each field came from.
"""


class Provenance:

    def add_source(self, candidate):
        """
        Add provenance information to every field.
        """

        provenance = {
            "name": "Resume",
            "email": "Resume",
            "phone": "Resume",
            "location": "Resume",
            "skills": "Resume",
            "education": "Resume",
            "experience": "Resume",
            "company": "Recruiter CSV",
            "designation": "Recruiter CSV"
        }

        candidate["provenance"] = provenance

        return candidate