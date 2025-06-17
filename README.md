# Flashcard-Generator-LLM-

# LLM-Powered Flashcard Generator (Hugging Face)

This project is a lightweight AI tool that converts educational content into high-quality flashcards using a transformer-based language model (`flan-t5-base`) from Hugging Face. It's designed for offline or low-cost usage — no OpenAI key required!

---

##  Features

Upload or paste educational text  
Automatically generate 10 question-answer flashcards  
Works with `.pdf`, `.txt`, or direct input  
Export flashcards to `.csv`  
Clean and minimal Streamlit interface  
Offline, open-source model (no API cost!)

---

## Tech Stack

| Component       | Technology               |
|----------------|---------------------------|
| Language Model  | `flan-t5-base` (Hugging Face) |
| Backend         | Python, PyTorch           |
| Frontend        | Streamlit                 |
| PDF Extraction  | PyMuPDF (`fitz`)          |
| File Export     | Pandas                    |



