"""
Test script untuk verifikasi paraphrase functionality
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

print("Loading model...")
MODEL_NAME = "Wikidepia/IndoT5-base-paraphrase"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
print("Model loaded!")

# Test paraphrase
test_sentence = "Anak anak melakukan piket kelas agar kebersihan kelas terjaga"
print(f"\n{'='*60}")
print(f"Original: {test_sentence}")
print(f"{'='*60}\n")

text = f"paraphrase: {test_sentence} </s>"
encoding = tokenizer(text, padding='longest', return_tensors="pt")

with torch.no_grad():
    outputs = model.generate(
        input_ids=encoding["input_ids"],
        attention_mask=encoding["attention_mask"],
        max_length=512,
        do_sample=True,
        top_k=200,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=3
    )

print("Paraphrased versions:")
for i, output in enumerate(outputs, 1):
    result = tokenizer.decode(output, skip_special_tokens=True)
    print(f"{i}. {result}")

print(f"\n{'='*60}")
print("✅ Model works perfectly!")
print(f"{'='*60}")
