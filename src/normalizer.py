"""
normalizer.py

Normalizes extracted candidate data.
"""

import re


class Normalizer:

    def normalize_email(self, email):
        """
        Convert email to lowercase.
        """
        if not email:
            return ""

        return email.strip().lower()

    def normalize_phone(self, phone):
        """
        Remove spaces and convert to standard format.
        """

        if not phone:
            return ""

        phone = re.sub(r"\D", "", phone)

        if phone.startswith("91") and len(phone) == 12:
            return "+" + phone

        elif len(phone) == 10:
            return "+91" + phone

        return phone

    def normalize_name(self, name):
        """
        Convert name to title case.
        """

        if not name:
            return ""

        return name.strip().title()

    def normalize_location(self, location):
        """
        Remove unwanted spaces.
        """

        if not location:
            return ""

        return " ".join(location.split())

    def normalize_skills(self, skills):
        """
        Remove duplicates and normalize skill names.
        """

        skill_map = {
            "python": "Python",
            "java": "Java",
            "javascript": "JavaScript",
            "react": "React",
            "reactjs": "React",
            "sql": "SQL",
            "git": "Git",
            "machine learning": "Machine Learning",
            "mongodb": "MongoDB",
            "html": "HTML",
            "css": "CSS"
        }

        normalized = []

        for skill in skills:

            key = skill.strip().lower()

            if key in skill_map:
                normalized.append(skill_map[key])
            else:
                normalized.append(skill.title())

        return list(dict.fromkeys(normalized))

    def normalize(self, candidate):
        """
        Normalize all extracted fields.
        """

        candidate["name"] = self.normalize_name(candidate["name"])

        candidate["email"] = self.normalize_email(candidate["email"])

        candidate["phone"] = self.normalize_phone(candidate["phone"])

        candidate["location"] = self.normalize_location(candidate["location"])

        candidate["skills"] = self.normalize_skills(candidate["skills"])

        return candidate