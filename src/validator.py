"""
validator.py

Validates candidate profile.
"""

import re


class Validator:

    def validate(self, candidate):

        errors = []

        # Required fields
        required_fields = [
            "name",
            "email",
            "phone",
            "company",
            "designation"
        ]

        for field in required_fields:

            value = candidate.get(field)

            if not value:
                errors.append(f"{field} is missing.")

        # Email validation
        email = candidate.get("email", "")

        if email:
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

            if not re.match(pattern, email):
                errors.append("Invalid email format.")

        # Phone validation
        phone = candidate.get("phone", "")

        if phone:

            digits = re.sub(r"\D", "", phone)

            if len(digits) != 12:
                errors.append("Invalid phone number.")

        candidate["validation"] = {

            "is_valid": len(errors) == 0,

            "errors": errors

        }

        return candidate