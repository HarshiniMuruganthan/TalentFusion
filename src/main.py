"""
main.py

TalentFusion - Intelligent Candidate Data Transformation Pipeline
"""

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


def main():

    # -------------------------------
    # Initialize Modules
    # -------------------------------

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

    # -------------------------------
    # Load Configuration
    # -------------------------------

    config = config_loader.load()

    # -------------------------------
    # Read Input Files
    # -------------------------------

    csv_data = reader.read_csv("input/recruiter.csv")
    resume_text = reader.read_resume("input/resume.pdf")

    # -------------------------------
    # Pipeline Starts
    # -------------------------------

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

    # -------------------------------
    # Generate JSON
    # -------------------------------

    output_file = generator.generate(candidate)

    # -------------------------------
    # Display Summary
    # -------------------------------

    print("\n" + "=" * 45)
    print("      TalentFusion Pipeline Completed")
    print("=" * 45)

    print(f"\nCandidate Name      : {candidate['name']}")
    print(f"Email               : {candidate['email']}")
    print(f"Company             : {candidate['company']}")
    print(f"Designation         : {candidate['designation']}")

    if config["enable_confidence"]:
        print(f"Overall Confidence  : {candidate['overall_confidence']}")

    if config["enable_profile_health"]:
        print(f"Profile Completion  : {candidate['profile_health']['completion']}%")
        print(f"Trust Score         : {candidate['profile_health']['trust_score']}")
        print(f"Profile Status      : {candidate['profile_health']['status']}")

    if config["enable_validation"]:
        print(f"Validation Status   : {candidate['validation']['is_valid']}")

    print(f"\nJSON Saved To       : {output_file}")

    print("\nPipeline executed successfully.")

    print("\n" + "=" * 45)
    print("FINAL CANDIDATE PROFILE")
    print("=" * 45)

    for key, value in candidate.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()