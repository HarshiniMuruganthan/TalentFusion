# TalentFusion – Intelligent Candidate Data Transformation Pipeline
## Overview

TalentFusion is an intelligent backend pipeline that transforms candidate information collected from multiple sources into a single, structured, and reliable candidate profile.

The system processes a candidate's resume and recruiter CSV data, extracts relevant information, normalizes the data, resolves conflicts, validates the profile, evaluates data quality, and generates a unified output with complete traceability.

## Features

- Resume Information Extraction
- Data Normalization
- Multi-Source Data Merging
- Conflict Resolution Engine
- Provenance Tracking
- Confidence Score Calculation
- Business Rule Validation
- Data Quality Assessment
- Profile Health Analysis
- Candidate Validation
- Transformation Report Generation
- Audit Trail Logging

## Project Structure

TalentFusion/
│
├── input/
│   ├── resume.pdf
│   └── recruiter.csv
│
├── output/
│   ├── result.json
│   ├── transformation_report.json
│   └── audit_log.json
│
├── reader.py
├── extractor.py
├── normalizer.py
├── merger.py
├── resolver.py
├── provenance.py
├── confidence.py
├── analyzer.py
├── validator.py
├── generator.py
├── report.py
├── audit.py
├── rule_engine.py
├── data_quality.py
├── config_loader.py
├── main.py
├── config.json
├── requirements.txt
└── README.md

## Technologies Used

- Python 3
- Regular Expressions
- JSON
- CSV
- Object-Oriented Programming

## Installation

Clone the repository.

```bash
git clone https://github.com/your-username/TalentFusion.git
cd TalentFusion
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the pipeline using:

```bash
python main.py
```

---

## Input Files

Place the following files inside the **input/** folder.

```
input/
├── resume.pdf
└── recruiter.csv
```

---

## Output Files

After successful execution, the following files are generated inside the **output/** directory.

```
output/
├── result.json
├── transformation_report.json
└── audit_log.json
```

---

## Pipeline Workflow

```
Resume + Recruiter CSV
          │
          ▼
Reader
          │
          ▼
Extractor
          │
          ▼
Normalizer
          │
          ▼
Merger
          │
          ▼
Conflict Resolver
          │
          ▼
Provenance Tracking
          │
          ▼
Confidence Engine
          │
          ▼
Rule Engine
          │
          ▼
Validator
          │
          ▼
Data Quality
          │
          ▼
Profile Health
          │
          ▼
JSON Output + Report + Audit Log
```

---

## Sample Output

The pipeline produces:

- Unified Candidate Profile
- Overall Confidence Score
- Data Quality Score
- Profile Health Report
- Conflict Report
- Validation Status
- Transformation Report
- Audit Trail

---

## Design Highlights

- Modular architecture with independent processing stages.
- Configurable pipeline using `config.json`.
- Automatic conflict resolution for inconsistent data.
- Provenance tracking for every extracted field.
- Complete audit trail for transparency and traceability.

---

## Edge Case Handled

The system detects conflicting information between the resume and recruiter CSV.

Example:

Resume Phone:

```
+91 9876543210
```

Recruiter CSV Phone:

```
9876543210
```

The Conflict Resolution Engine identifies the mismatch, applies predefined business rules to determine the preferred value, records the selected result, and logs the decision in the audit trail.

---

## Future Enhancements

- OCR support for scanned resumes.
- AI/LLM-based resume parsing.
- Database integration.
- REST API support.
- Interactive web dashboard.
- Cloud deployment.

---

## Author

*Harshini M*
B.E. Computer Science and Engineering
TalentFusion – Intelligent Candidate Data Transformation Pipeline
