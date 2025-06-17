import os
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

import streamlit as st
import pandas as pd
from flashcard_generator import generate_flashcards
from utils import extract_text_from_pdf, parse_flashcards
from io import StringIO

st.set_page_config(page_title="Flashcard Generator")
st.title("LLM Flashcard Generator")

input_method = st.radio("Choose input method:", ["Upload File", "Paste Text"])
subject = st.text_input("Optional: Subject (e.g., Biology, History)")
text_data = ""

if input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            text_data = extract_text_from_pdf(uploaded_file)
        else:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            text_data = stringio.read()
elif input_method == "Paste Text":
    text_data = st.text_area("Paste your text here")

if st.button("Generate Flashcards"):
    if not text_data.strip():
        st.warning("Please provide input data.")
    else:
        raw_output = generate_flashcards(text_data, subject)
        st.text_area("🧪 Raw Model Output", raw_output, height=300)

        flashcards = parse_flashcards(raw_output)

        if flashcards:
            st.success(f"✅ Generated {len(flashcards)} flashcards!")
            for card in flashcards:
                st.markdown(f"**Q:** {card['Question']}")
                st.markdown(f"**A:** {card['Answer']}")
                st.markdown("---")

            df = pd.DataFrame(flashcards)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download CSV", data=csv, file_name="flashcards.csv", mime="text/csv")
        else:
            st.warning("⚠️ No flashcards were generated. Check the raw output and prompt format.")
