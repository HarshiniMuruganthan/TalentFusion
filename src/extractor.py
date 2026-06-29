"""
extractor.py

Extract structured information from resume text.
"""

import re


class Extractor:

    def extract_name(self, text):
        """Extract candidate name (first non-empty line)."""
        for line in text.split("\n"):
            line = line.strip()
            if line:
                return line
        return ""

    def extract_email(self, text):
        """Extract email address."""
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
        return match.group(0) if match else ""

    def extract_phone(self, text):
        """Extract Indian phone number."""
        match = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', text)

        if match:
            phone = match.group(0)
            phone = phone.replace(" ", "").replace("-", "")

            if not phone.startswith("+91"):
                if phone.startswith("91"):
                    phone = "+" + phone
                else:
                    phone = "+91" + phone

            return phone

        return ""

    def extract_location(self, text):
        """Extract location."""

        lines = text.split("\n")

        for i, line in enumerate(lines):

            if line.strip().lower() == "location:":

                if i + 1 < len(lines):
                    return lines[i + 1].strip()

        return ""

    def extract_skills(self, text):
        """Extract technical skills."""

        skills = [
            "Python",
            "Java",
            "SQL",
            "JavaScript",
            "React",
            "Node.js",
            "Machine Learning",
            "Git",
            "MongoDB",
            "HTML",
            "CSS",
            "C++"
        ]

        found = []

        lower_text = text.lower()

        for skill in skills:
            if skill.lower() in lower_text:
                found.append(skill)

        return list(dict.fromkeys(found))

    def extract_education(self, text):
        """Extract education."""

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

        for line in text.split("\n"):

            for keyword in keywords:

                if keyword.lower() in line.lower():
                    education.append(line.strip())

        return education

    def extract_experience(self, text):
        """Extract experience section."""

        experience = []

        lines = text.split("\n")

        capture = False

        for line in lines:

            line = line.strip()

            if line.upper() == "EXPERIENCE":
                capture = True
                continue

            if line.upper() == "EDUCATION":
                break

            if capture and line:
                experience.append(line)

        return experience

    def extract_all(self, text):
        """Extract all candidate details."""

        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "location": self.extract_location(text),
            "skills": self.extract_skills(text),
            "education": self.extract_education(text),
            "experience": self.extract_experience(text)
        }