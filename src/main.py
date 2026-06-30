"""
main.py

TalentFusion - Intelligent Candidate Data Transformation Pipeline
"""

import time

from reader import Reader
from extractor import Extractor
from normalizer import Normalizer
from merger import Merger
from provenance import Provenance
from confidence import Confidence
from analyzer import Analyzer
from validator import Validator
from generator import Generator
from config_loader import ConfigLoader
from report import Report


def main():

    # -----------------------------------------
    # Start Timer
    # -----------------------------------------

    start_time = time.time()

    # -----------------------------------------
    # Initialize Modules
    # -----------------------------------------

    reader = Reader()
    extractor = Extractor()
    normalizer = Normalizer()
    merger = Merger()
    provenance = Provenance()
    confidence = Confidence()
    analyzer = Analyzer()
    validator = Validator()
    generator = Generator()
    config_loader = ConfigLoader()
    report = Report()

    # -----------------------------------------
    # Load Configuration
    # -----------------------------------------

    config = config_loader.load()

    # -----------------------------------------
    # Read Input Files
    # -----------------------------------------

    csv_data = reader.read_csv("input/recruiter.csv")
    resume_text = reader.read_resume("input/resume.pdf")

    # -----------------------------------------
    # Execute Pipeline
    # -----------------------------------------

    candidate = extractor.extract_all(resume_text)

    candidate = normalizer.normalize(candidate)

    candidate = merger.merge(candidate, csv_data)

    if config["enable_provenance"]:
        candidate = provenance.add_source(candidate)

    if config["enable_confidence"]:
        candidate = confidence.calculate(candidate)

    if config["enable_profile_health"]:
        candidate = analyzer.analyze(candidate)

    if config["enable_validation"]:
        candidate = validator.validate(candidate)

    # -----------------------------------------
    # Generate Output Files
    # -----------------------------------------

    output_file = generator.generate(candidate)

    report_file = report.generate(candidate, start_time)

    # -----------------------------------------
    # Display Dashboard
    # -----------------------------------------

    print("\n")
    print("=" * 55)
    print("           TALENTFUSION DASHBOARD")
    print("=" * 55)

    print("\nCandidate Information")
    print("-" * 55)
    print(f"Name                : {candidate['name']}")
    print(f"Email               : {candidate['email']}")
    print(f"Company             : {candidate['company']}")
    print(f"Designation         : {candidate['designation']}")
    print(f"Location            : {candidate['location']}")

    print("\nPipeline Metrics")
    print("-" * 55)

    if config["enable_confidence"]:
        print(f"Overall Confidence  : {candidate['overall_confidence']}")

    if config["enable_profile_health"]:
        print(f"Profile Completion  : {candidate['profile_health']['completion']}%")
        print(f"Trust Score         : {candidate['profile_health']['trust_score']}")
        print(f"Profile Status      : {candidate['profile_health']['status']}")

    if config["enable_validation"]:
        print(f"Validation Status   : {'PASSED' if candidate['validation']['is_valid'] else 'FAILED'}")

    print(f"Skills Extracted    : {len(candidate['skills'])}")
    print(f"Education Records   : {len(candidate['education'])}")
    print(f"Experience Records  : {len(candidate['experience'])}")

    print("\nGenerated Files")
    print("-" * 55)
    print(f"Candidate JSON      : {output_file}")
    print(f"Transformation Report : {report_file}")

    print("\nPipeline Status")
    print("-" * 55)
    print("Pipeline executed successfully.")

    print("\n")
    print("=" * 55)
    print("FINAL CANDIDATE PROFILE")
    print("=" * 55)

    for key, value in candidate.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()