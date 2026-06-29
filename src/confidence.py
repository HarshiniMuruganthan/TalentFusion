"""
confidence.py

Calculates confidence score for candidate data.
"""


class Confidence:

    def calculate(self, candidate):
        """
        Assign confidence scores based on source.
        """

        scores = {}

        # Resume fields
        scores["name"] = 0.99
        scores["email"] = 0.98
        scores["phone"] = 0.97
        scores["location"] = 0.95
        scores["skills"] = 0.96
        scores["education"] = 0.95
        scores["experience"] = 0.94

        # CSV fields
        scores["company"] = 0.90
        scores["designation"] = 0.90

        candidate["confidence"] = scores

        candidate["overall_confidence"] = round(
            sum(scores.values()) / len(scores), 2
        )

        return candidate