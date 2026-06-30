"""
data_quality.py

Calculates data quality score for candidate profile.
Enterprise-grade scoring with consistent validation.
"""

class DataQuality:

    def evaluate(self, candidate):

        fields = [
            "name",
            "email",
            "phone",
            "location",
            "skills",
            "education",
            "experience"
        ]

        total_fields = len(fields)
        filled = 0

        # -----------------------------
        # COMPLETENESS CHECK
        # -----------------------------
        for f in fields:
            value = candidate.get(f)

            if isinstance(value, list):
                if len(value) > 0:
                    filled += 1

            elif isinstance(value, str):
                if value.strip():
                    filled += 1

        completeness = int((filled / total_fields) * 100)

        # -----------------------------
        # ACCURACY SCORE
        # -----------------------------
        accuracy = int(candidate.get("overall_confidence", 0) * 100)

        # -----------------------------
        # CONSISTENCY SCORE
        # (based on conflicts)
        # -----------------------------
        conflicts = candidate.get("conflicts", [])
        consistency = 100 - (len(conflicts) * 10)

        if consistency < 0:
            consistency = 0

        # -----------------------------
        # VALIDITY SCORE (FIXED)
        # -----------------------------
        is_valid = candidate.get("validation", {}).get("is_valid", False)
        validity = 100 if is_valid else 0

        # -----------------------------
        # OVERALL SCORE
        # -----------------------------
        overall = int((completeness + accuracy + consistency + validity) / 4)

        # -----------------------------
        # GRADE ASSIGNMENT
        # -----------------------------
        if overall >= 90:
            grade = "A+"
        elif overall >= 80:
            grade = "A"
        elif overall >= 70:
            grade = "B"
        elif overall >= 60:
            grade = "C"
        else:
            grade = "D"

        # -----------------------------
        # ATTACH RESULT
        # -----------------------------
        candidate["data_quality"] = {
            "completeness": completeness,
            "accuracy": accuracy,
            "consistency": consistency,
            "validity": validity,
            "overall_score": overall,
            "grade": grade
        }

        return candidate