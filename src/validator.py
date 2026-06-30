"""
validator.py
"""

import re


class Validator:

    def validate(self, candidate):

        errors = []

        # Name
        if not candidate.get("name"):
            errors.append("Name missing.")

        # Email
        email = candidate.get("email", "")

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            errors.append("Invalid email.")

        # Phone
        phone = candidate.get("phone", "")

        # Remove symbols
        digits = re.sub(r"\D", "", phone)

        valid = False

        if len(digits) == 10:
            valid = True

        elif len(digits) == 12 and digits.startswith("91"):
            valid = True

        if not valid:
            errors.append("Invalid phone number.")

        # Skills
        if len(candidate.get("skills", [])) == 0:
            errors.append("No skills found.")

        candidate["validation"] = {
            "is_valid": len(errors) == 0,
            "errors": errors
        }

        return candidate