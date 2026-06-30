"""
normalizer.py

Normalize candidate information.
"""

import re


class Normalizer:

    def normalize(self, candidate):

        # Name
        if candidate.get("name"):
            candidate["name"] = candidate["name"].strip().title()

        # Email
        if candidate.get("email"):
            candidate["email"] = candidate["email"].strip().lower()

        # Phone
        if candidate.get("phone"):

            phone = str(candidate["phone"])

            # Remove everything except digits
            phone = re.sub(r"\D", "", phone)

            # Handle 12 digits starting with 91
            if len(phone) == 12 and phone.startswith("91"):
                phone = phone[2:]

            # Convert 10-digit number to +91 format
            if len(phone) == 10:
                phone = "+91" + phone

            candidate["phone"] = phone

        # Location
        if candidate.get("location"):
            candidate["location"] = candidate["location"].strip().title()

        # Skills
        if candidate.get("skills"):

            skills = []

            for skill in candidate["skills"]:

                skill = skill.strip()

                if skill not in skills:
                    skills.append(skill)

            candidate["skills"] = skills

        return candidate