"""
main.py

TalentFusion - Intelligent Candidate Data Transformation Pipeline
"""

import time

from reader import Reader
from extractor import Extractor
from normalizer import Normalizer
from merger import Merger
from resolver import Resolver
from provenance import Provenance
from confidence import Confidence
from analyzer import Analyzer
from validator import Validator
from generator import Generator
from config_loader import ConfigLoader
from report import Report
from audit import Audit
from rule_engine import RuleEngine
from data_quality import DataQuality


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
    resolver = Resolver()
    provenance = Provenance()
    confidence = Confidence()
    analyzer = Analyzer()
    validator = Validator()
    generator = Generator()
    config_loader = ConfigLoader()
    report = Report()
    audit = Audit()
    rule_engine = RuleEngine()
    data_quality = DataQuality()

    # -----------------------------------------
    # Load Configuration
    # -----------------------------------------
    config = config_loader.load()

    # -----------------------------------------
    # Read Input Files
    # -----------------------------------------

    csv_data = reader.read_csv("input/recruiter.csv")
    audit.log(
        "Reader",
        "Recruiter CSV Loaded",
        "recruiter.csv successfully loaded"
    )

    resume_text = reader.read_resume("input/resume.pdf")
    audit.log(
        "Reader",
        "Resume Loaded",
        "resume.pdf successfully loaded"
    )

    # -----------------------------------------
    # Execute Pipeline
    # -----------------------------------------

    # Step 1 - Extract
    candidate = extractor.extract_all(resume_text)

    audit.log(
        "Extractor",
        "Candidate Extracted",
        f"Candidate: {candidate.get('name')}"
    )

    # Step 2 - Normalize
    candidate = normalizer.normalize(candidate)

    audit.log(
        "Normalizer",
        "Normalization Completed",
        "Name, Email and Phone normalized"
    )

    # Step 3 - Merge
    candidate = merger.merge(candidate, csv_data)

    audit.log(
        "Merger",
        "Merge Completed",
        "Resume merged with Recruiter CSV"
    )

    # Step 4 - Resolve Conflicts
    candidate = resolver.resolve(candidate, csv_data)

    audit.log(
        "Resolver",
        "Conflict Resolution",
        f"{len(candidate['conflicts'])} conflicts detected"
    )

    # Normalize again after conflict resolution
    candidate = normalizer.normalize(candidate)

    audit.log(
        "Normalizer",
        "Post Merge Normalization",
        "Final data standardized"
    )

    # Step 5 - Provenance
    if config["enable_provenance"]:
        candidate = provenance.add_source(candidate)

        audit.log(
            "Provenance",
            "Source Mapping Completed"
        )
# -----------------------------------------
# Step 6 - Confidence
# -----------------------------------------

    if config["enable_confidence"]:

        candidate = confidence.calculate(candidate)

        audit.log(
             "Confidence",
             "Confidence Calculated",
             f"Overall Confidence = {candidate['overall_confidence']}"
    )

# -----------------------------------------
# Step 6.5 - Rule Engine
# -----------------------------------------

    if config.get("enable_rule_engine", True):

        candidate = rule_engine.evaluate(candidate)

        audit.log(
            "Rule Engine",
            "Business Rules Evaluated",
            "All hiring rules checked"
    )

# -----------------------------------------
# Step 7 - Profile Health
# -----------------------------------------

    if config["enable_profile_health"]:

        candidate = analyzer.analyze(candidate)

        audit.log(
            "Analyzer",
            "Profile Health Generated"
    )

# -----------------------------------------
# Step 8 - Validation
# -----------------------------------------

    if config["enable_validation"]:

        candidate = validator.validate(candidate)

        audit.log(
            "Validator",
            "Validation Completed",
            f"Status = {candidate['validation']['is_valid']}"
    )

# -----------------------------------------
# Step 9 - Data Quality
# (Must run AFTER validation)
# -----------------------------------------

    if config.get("enable_data_quality", True):

        candidate = data_quality.evaluate(candidate)

        audit.log(
            "Data Quality",
            "Quality Score Calculated",
            f"Overall Score = {candidate['data_quality']['overall_score']}"
    )

    # -----------------------------------------
    # Generate Output Files
    # -----------------------------------------

    output_file = generator.generate(candidate)

    audit.log(
        "Generator",
        "Candidate JSON Generated",
        output_file
    )

    report_file = report.generate(candidate, start_time)

    audit.log(
        "Report",
        "Transformation Report Generated",
        report_file
    )

    audit.log(
        "Pipeline",
        "Execution Completed"
    )

    audit_file = audit.save()

    # -----------------------------------------
    # Dashboard
    # -----------------------------------------

    print("\n")
    print("=" * 60)
    print("              TALENTFUSION DASHBOARD")
    print("=" * 60)

    print("\nCandidate Information")
    print("-" * 60)
    print(f"Name                : {candidate['name']}")
    print(f"Email               : {candidate['email']}")
    print(f"Phone               : {candidate['phone']}")
    print(f"Company             : {candidate['company']}")
    print(f"Designation         : {candidate['designation']}")
    print(f"Location            : {candidate['location']}")

    print("\nPipeline Metrics")
    print("-" * 60)

    if config["enable_confidence"]:
        print(f"Overall Confidence  : {candidate['overall_confidence']}")

    if config["enable_profile_health"]:
        print(f"Profile Completion  : {candidate['profile_health']['completion']}%")
        print(f"Trust Score         : {candidate['profile_health']['trust_score']}")
        print(f"Profile Status      : {candidate['profile_health']['status']}")

    if config["enable_validation"]:
        status = "PASSED" if candidate["validation"]["is_valid"] else "FAILED"
        print(f"Validation Status   : {status}")

    print(f"Skills Extracted    : {len(candidate['skills'])}")
    print(f"Education Records   : {len(candidate['education'])}")
    print(f"Experience Records  : {len(candidate['experience'])}")

    print("\nGenerated Files")
    print("-" * 60)
    print(f"Candidate JSON        : {output_file}")
    print(f"Transformation Report : {report_file}")
    print(f"Audit Log             : {audit_file}")

    print("\nPipeline Status")
    print("-" * 60)
    print("Pipeline executed successfully.")

    # -----------------------------------------
    # Final Candidate Profile
    # -----------------------------------------

    print("\n")
    print("=" * 60)
    print("FINAL CANDIDATE PROFILE")
    print("=" * 60)

    for key, value in candidate.items():
        print(f"{key}: {value}")

    # -----------------------------------------
    # Conflict Report
    # -----------------------------------------

    print("\n")
    print("=" * 60)
    print("CONFLICT REPORT")
    print("=" * 60)

    if candidate.get("conflicts"):

        for conflict in candidate["conflicts"]:

            print(f"\nField        : {conflict['field']}")
            print(f"Resume Value : {conflict['resume_value']}")
            print(f"CSV Value    : {conflict['csv_value']}")
            print(f"Selected     : {conflict['selected_value']}")
            print(f"Winner       : {conflict['winner']}")
            print(f"Reason       : {conflict['reason']}")

    else:

        print("No conflicts found.")

    # -----------------------------------------
    # Audit Trail
    # -----------------------------------------

    print("\n")
    print("=" * 60)
    print("AUDIT TRAIL")
    print("=" * 60)

    for log in audit.logs:

        print(
            f"[{log['timestamp']}] "
            f"{log['module']} -> "
            f"{log['action']}"
        )


if __name__ == "__main__":
    main()