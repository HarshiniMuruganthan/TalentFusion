import re


class Extractor:

    def extract_name(self, text):
        lines = text.split("\n")

        for line in lines:
            if line.strip():
                return line.strip()

        return ""


    def extract_email(self, text):
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

        if match:
            return match.group()

        return ""


    def extract_phone(self, text):
        match = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', text)

        if match:
            return match.group()

        return ""


    def extract_location(self, text):

        lines = text.split("\n")

        for i, line in enumerate(lines):

            if line.strip().lower() == "location:":

                if i + 1 < len(lines):
                    return lines[i + 1].strip()

        return ""
        def extract_skills(self, text):

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

            for word in keywords:

                if word.lower() in line.lower():
                    education.append(line.strip())

        return education
        def extract_experience(self, text):

        experience = []

        lines = text.split("\n")

        capture = False

        for line in lines:

            if "EXPERIENCE" in line.upper():
                capture = True
                continue

            if "EDUCATION" in line.upper():
                break

            if capture and line.strip():
                experience.append(line.strip())

        return experience
        def extract_all(self, text):

        return {

            "name": self.extract_name(text),

            "email": self.extract_email(text),

            "phone": self.extract_phone(text),

            "location": self.extract_location(text),

            "skills": self.extract_skills(text),

            "education": self.extract_education(text),

            "experience": self.extract_experience(text)

        }