"""
extractor.py

Extracts structured information from resume text.
"""

import re


class Extractor:
    """
    Extract important candidate information from resume text.
    """

    def extract_name(self, text):
        """
        Assume the first non-empty line is the candidate's name.
        """
        lines = text.split("\n")

        for line in lines:
            if line.strip():
                return line.strip()

        return ""

    def extract_email(self, text):
        """
        Extract email using regex.
        """
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

        if match:
            return match.group()

        return ""

    def extract_phone(self, text):
        """
        Extract Indian phone number.
        """
        match = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', text)

        if match:
            return match.group()

        return ""

    def extract_location(self, text):
        """
        Extract location from resume.
        """
        lines = text.split("\n")

        for i, line in enumerate(lines):

            if line.strip().lower() == "location:":

                if i + 1 < len(lines):
                    return lines[i + 1].strip()

        return ""

    def extract_skills(self, text):
        """
        Extract known technical skills.
        """

        skill_list = [
            "Python",
            "Java",
            "C",
            "C++",
            "SQL",
            "React",
            "Node.js",
            "JavaScript",
            "Machine Learning",
            "HTML",
            "CSS",
            "Git",
            "MongoDB"
        ]

        found = []

        lower_text = text.lower()

        for skill in skill_list:
            if skill.lower() in lower_text:
                found.append(skill)

        return found

    def extract_education(self, text):
        """
        Extract education details.
        """

        education = []

        keywords = [
            "B.E",
            "B.Tech",
            "M.E",
            "M.Tech",
            "B.Sc",
            "M.Sc",
            "MBA"
        ]

        lines = text.split("\n")

        for line in lines:
            for keyword in keywords:
                if keyword.lower() in line.lower():
                    education.append(line.strip())

        return education

    def extract_experience(self, text):
        """
        Extract experience section.
        """

        experience = []

        lines = text.split("\n")

        capture = False

        for line in lines:

            if "EXPERIENCE" in line.upper():
                capture = True
                continue

            if "EDUCATION" in line.upper():
                break

            if capture:
                if line.strip():
                    experience.append(line.strip())

        return experience

    def extract_all(self, text):
        """
        Extract all candidate information.
        """

        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "location": self.extract_location(text),
            "skills": self.extract_skills(text),
            "education": self.extract_education(text),
            "experience": self.extract_experience(text)
        }