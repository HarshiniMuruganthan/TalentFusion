"""
rule_engine.py

Validates candidate against hiring/business rules.
"""

class RuleEngine:

    def __init__(self):

        # Define hiring rules (customize anytime)
        self.rules = [
            ("has_email", "Email is required"),
            ("has_phone", "Phone is required"),
            ("has_name", "Name is required"),
            ("min_skills", "At least 3 skills required"),
            ("valid_confidence", "Confidence must be >= 0.80"),
        ]

    def evaluate(self, candidate):

        failed_rules = []

        # Rule 1: Email
        if not candidate.get("email"):
            failed_rules.append("Email is required")

        # Rule 2: Phone
        if not candidate.get("phone"):
            failed_rules.append("Phone is required")

        # Rule 3: Name
        if not candidate.get("name"):
            failed_rules.append("Name is required")

        # Rule 4: Skills count
        if len(candidate.get("skills", [])) < 3:
            failed_rules.append("At least 3 skills required")

        # Rule 5: Confidence threshold
        if candidate.get("overall_confidence", 0) < 0.80:
            failed_rules.append("Confidence must be >= 0.80")

        passed = len(failed_rules) == 0

        candidate["rule_engine"] = {
            "passed": passed,
            "failed_rules": failed_rules
        }

        return candidate