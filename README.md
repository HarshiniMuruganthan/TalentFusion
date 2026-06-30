# TalentFusion – Intelligent Candidate Data Transformation Pipeline

## Overview

TalentFusion is an intelligent candidate data transformation pipeline that consolidates information from multiple data sources into a single, structured, and reliable candidate profile.

The system extracts information from a candidate's resume and recruiter CSV, normalizes the data, merges records, resolves conflicts, validates the final profile, calculates confidence and quality scores, and generates a complete transformation report along with an audit trail.

---

## Features

- Resume Information Extraction
- Data Normalization
- Multi-Source Data Merging
- Conflict Resolution
- Provenance Tracking
- Confidence Score Calculation
- Business Rule Validation
- Data Quality Assessment
- Profile Health Analysis
- Candidate Validation
- Transformation Report Generation
- Audit Trail Logging

---

# Project Structure

```text
TalentFusion/
│
├── input/
│   ├── recruiter.csv
│   └── resume.pdf
│
├── output/
│   ├── audit_log.json
│   ├── result.json
│   └── transformation_report.json
│
├── analyzer.py
├── audit.py
├── confidence.py
├── config.json
├── config_loader.py
├── data_quality.py
├── extractor.py
├── generator.py
├── main.py
├── merger.py
├── normalizer.py
├── provenance.py
├── reader.py
├── report.py
├── requirements.txt
├── resolver.py
├── rule_engine.py
├── validator.py
└── README.md
```

---

# Technologies Used

- Python 3
- Regular Expressions (Regex)
- JSON
- CSV
- Object-Oriented Programming (OOP)

---

# Installation

Clone the repository.

```bash
git clone https://github.com/HarshiniMuruganthan/TalentFusion.git
```

Move to the project directory.

```bash
cd TalentFusion
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Project

Execute the pipeline using:

```bash
python main.py
```

---

# Input Files

Place the following files inside the **input** directory.

```text
input/
├── recruiter.csv
└── resume.pdf
```

---

# Output Files

After execution, the generated files will be available inside the **output** directory.

```text
output/
├── audit_log.json
├── result.json
└── transformation_report.json
```

---

# Pipeline Workflow

```text
Resume PDF + Recruiter CSV
            │
            ▼
         Reader
            │
            ▼
       Information
       Extraction
            │
            ▼
     Data Normalization
            │
            ▼
      Multi-Source Merge
            │
            ▼
    Conflict Resolution
            │
            ▼
   Provenance Tracking
            │
            ▼
 Confidence Score Engine
            │
            ▼
    Business Rule Engine
            │
            ▼
     Candidate Validation
            │
            ▼
   Data Quality Analysis
            │
            ▼
    Profile Health Report
            │
            ▼
 JSON + Report + Audit Log
```

---

# Modules

| Module | Responsibility |
|---------|----------------|
| Reader | Reads input files |
| Extractor | Extracts candidate information |
| Normalizer | Standardizes extracted data |
| Merger | Merges resume and recruiter data |
| Resolver | Resolves conflicting values |
| Provenance | Tracks the source of every field |
| Confidence | Calculates confidence scores |
| Rule Engine | Applies business validation rules |
| Validator | Validates the candidate profile |
| Data Quality | Measures profile quality |
| Analyzer | Generates profile health metrics |
| Generator | Produces final JSON output |
| Report | Generates transformation report |
| Audit | Records every pipeline operation |

---

# Sample Output

The pipeline generates:

- Unified Candidate Profile
- Overall Confidence Score
- Data Quality Score
- Profile Health Report
- Validation Status
- Conflict Report
- Transformation Report
- Audit Trail

---

# Design Highlights

- Modular pipeline architecture.
- Configurable processing through `config.json`.
- Automatic conflict resolution between multiple sources.
- Provenance tracking for every extracted field.
- Confidence and quality scoring.
- Complete audit logging for traceability.

---

# Edge Case Handled

The system handles conflicting information from multiple data sources.

Example:

**Resume**

```text
Phone : +91 9876543210
```

**Recruiter CSV**

```text
Phone : 9876543210
```

The Conflict Resolution Engine detects the mismatch, applies predefined business rules to determine the preferred value, records the selected value, and stores the decision in the audit trail.

---

# Future Enhancements

- OCR support for scanned resumes
- AI-powered resume parsing
- Database integration
- REST API support
- Interactive web dashboard
- Cloud deployment

---

# Author

**Harshini M**

Bachelor of Engineering – Computer Science and Engineering

TalentFusion – Intelligent Candidate Data Transformation Pipeline
