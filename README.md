# TalentFusion – Intelligent Candidate Data Transformation Pipeline

## Overview

TalentFusion is an intelligent backend pipeline that transforms candidate information collected from multiple sources into a single, structured, and reliable candidate profile.

The system processes a candidate's resume and recruiter CSV data, extracts relevant information, normalizes the data, resolves conflicts, validates the profile, evaluates data quality, and generates a unified output with complete traceability.

---

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

---

# Project Structure

```text
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
├── config.json
├── main.py
├── requirements.txt
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

Move into the project directory.

```bash
cd TalentFusion
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the pipeline using:

```bash
python main.py
```

---

# Input Files

Place the following files inside the **input** folder.

```text
input/
├── resume.pdf
└── recruiter.csv
```

---

# Output Files

After successful execution, the following files will be generated inside the **output** folder.

```text
output/
├── result.json
├── transformation_report.json
└── audit_log.json
```

---

# Pipeline Workflow

```text
Resume PDF
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
Provenance Tracker
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
Data Quality Engine
      │
      ▼
Profile Health Analyzer
      │
      ▼
JSON Generator
      │
      ▼
Transformation Report
      │
      ▼
Audit Log
```

---

# Modules

| Module | Description |
|---------|-------------|
| Reader | Reads resume PDF and recruiter CSV |
| Extractor | Extracts candidate details |
| Normalizer | Standardizes extracted data |
| Merger | Combines data from multiple sources |
| Resolver | Resolves conflicting values |
| Provenance | Tracks the source of each field |
| Confidence | Calculates confidence scores |
| Rule Engine | Applies business rules |
| Validator | Validates extracted data |
| Data Quality | Calculates quality metrics |
| Analyzer | Generates profile health |
| Generator | Creates final JSON output |
| Report | Generates transformation report |
| Audit | Maintains execution logs |

---

# Sample Output

The pipeline generates:

- Unified Candidate Profile
- Overall Confidence Score
- Data Quality Report
- Validation Status
- Conflict Report
- Profile Health Report
- Transformation Report
- Audit Trail

---

# Design Highlights

- Modular pipeline architecture.
- Configurable processing using `config.json`.
- Automatic conflict resolution.
- Provenance tracking for transparency.
- Confidence and quality scoring.
- Complete audit logging.

---

# Edge Case Handled

The system handles conflicting candidate information from different sources.

Example:

**Resume**

```text
Phone : +91 9876543210
```

**Recruiter CSV**

```text
Phone : 9876543210
```

The Conflict Resolution Engine detects the mismatch, selects the preferred value according to predefined business rules, and records the decision in the audit log.

---

# Future Enhancements

- OCR-based resume parsing
- AI-powered information extraction
- Database integration
- REST API support
- Web dashboard
- Cloud deployment

---

# Author

**Harshini M**

Bachelor of Engineering (Computer Science and Engineering)

TalentFusion – Intelligent Candidate Data Transformation Pipeline
