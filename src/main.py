from reader import Reader
from extractor import Extractor

reader = Reader()
extractor = Extractor()

resume = reader.read_resume("input/resume.pdf")

candidate = extractor.extract_all(resume)

print(candidate)