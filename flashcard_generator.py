
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_flashcards(text, subject=None):

    input_text = prefix + "\n" + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(inputs, max_length=1024, num_return_sequences=1)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result
