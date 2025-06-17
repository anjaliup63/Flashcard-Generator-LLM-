
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def parse_flashcards(raw_output):
    lines = raw_output.strip().split('\n')
    flashcards = []
    current_q = current_a = None

    for line in lines:
        if line.startswith("Q:"):
            current_q = line[2:].strip()
        elif line.startswith("A:"):
            current_a = line[2:].strip()
            if current_q:
                flashcards.append({"Question": current_q, "Answer": current_a})
                current_q = current_a = None
    return flashcards
