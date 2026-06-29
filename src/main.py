from reader import Reader
from extractor import Extractor
from normalizer import Normalizer
from merger import Merger

reader = Reader()
extractor = Extractor()
normalizer = Normalizer()
merger = Merger()

# Read data
csv_data = reader.read_csv("input/recruiter.csv")
resume_text = reader.read_resume("input/resume.pdf")

# Extract
candidate = extractor.extract_all(resume_text)

# Normalize
candidate = normalizer.normalize(candidate)

# Merge
candidate = merger.merge(candidate, csv_data)

print("\n===== MERGED CANDIDATE =====\n")

for key, value in candidate.items():
    print(f"{key}: {value}")