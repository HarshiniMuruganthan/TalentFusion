"""
merger.py

Merge resume data and recruiter CSV data.
"""


class Merger:

    def merge(self, resume_data, csv_data):
        """
        Merge candidate information.
        Resume has higher priority.
        """

        merged = {}

        # Resume data
        merged["name"] = resume_data.get("name", "")

        merged["email"] = resume_data.get("email", "")

        merged["phone"] = resume_data.get("phone", "")

        merged["location"] = resume_data.get("location", "")

        merged["skills"] = resume_data.get("skills", [])

        merged["education"] = resume_data.get("education", [])

        merged["experience"] = resume_data.get("experience", [])

        # CSV data
        merged["company"] = csv_data.get("Company", "")

        merged["designation"] = csv_data.get("Designation", "")

        return merged