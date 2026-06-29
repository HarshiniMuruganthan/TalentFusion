"""
reader.py

Reads candidate data from:
1. Recruiter CSV
2. Resume PDF
"""

import pandas as pd
import pdfplumber
from typing import Dict, Any


class Reader:
    """
    Reads all input sources.
    """

    def read_csv(self, csv_path: str) -> Dict[str, Any]:
        """
        Read recruiter CSV.
        Returns the first candidate as a dictionary.
        """

        try:
            df = pd.read_csv(csv_path)

            if df.empty:
                print("CSV file is empty.")
                return {}

            return df.iloc[0].to_dict()

        except Exception as e:
            print(f"Error reading CSV: {e}")
            return {}

    def read_resume(self, pdf_path: str) -> str:
        """
        Read resume PDF.
        Returns all extracted text.
        """

        try:
            text = ""

            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

            return text

        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""