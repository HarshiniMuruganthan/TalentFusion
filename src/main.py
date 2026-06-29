from reader import Reader
from extractor import Extractor
from normalizer import Normalizer
from merger import Merger
from provenance import Provenance

reader = Reader()
extractor = Extractor()
normalizer = Normalizer()
merger = Merger()
provenance = Provenance()

# Read input
csv_data = reader.read_csv("input/recruiter.csv")
resume_text = reader.read_resume("input/resume.pdf")

# Pipeline
candidate = extractor.extract_all(resume_text)
candidate = normalizer.normalize(candidate)
candidate = merger.merge(candidate, csv_data)
candidate = provenance.add_source(candidate)

print("\n===== FINAL CANDIDATE =====\n")

for key, value in candidate.items():
    print(f"{key}: {value}")