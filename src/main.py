from reader import Reader
from extractor import Extractor
from normalizer import Normalizer

reader = Reader()
extractor = Extractor()
normalizer = Normalizer()

resume_text = reader.read_resume("input/resume.pdf")

candidate = extractor.extract_all(resume_text)

candidate = normalizer.normalize(candidate)

print("\n===== NORMALIZED CANDIDATE =====\n")

print(candidate)