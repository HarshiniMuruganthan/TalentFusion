"""
analyzer.py

Analyzes candidate profile quality.
"""


class Analyzer:

    def analyze(self, candidate):

        required_fields = [
            "name",
            "email",
            "phone",
            "location",
            "company",
            "designation",
            "skills",
            "education",
            "experience"
        ]

        filled = 0
        missing = []

        for field in required_fields:

            value = candidate.get(field)

            if value:
                filled += 1
            else:
                missing.append(field)

        completion = round((filled / len(required_fields)) * 100)

        confidence = candidate.get("overall_confidence", 0)

        trust_score = round((completion + confidence * 100) / 2)

        if completion >= 90:
            status = "Excellent"

        elif completion >= 70:
            status = "Good"

        elif completion >= 50:
            status = "Average"

        else:
            status = "Poor"

        suggestions = []

        if "skills" in missing:
            suggestions.append("Add technical skills")

        if "education" in missing:
            suggestions.append("Add education details")

        if "experience" in missing:
            suggestions.append("Add work experience")

        if "location" in missing:
            suggestions.append("Add location")

        candidate["profile_health"] = {

            "completion": completion,

            "trust_score": trust_score,

            "status": status,

            "missing_fields": missing,

            "suggestions": suggestions
        }

        return candidate