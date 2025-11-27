import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re

# Load model dan tokenizer
print("Loading model...")
MODEL_NAME = "Wikidepia/IndoT5-base-paraphrase"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
print("Model loaded successfully!")

def split_into_paragraphs(text):
    """Split text into paragraphs, preserving empty lines"""
    # Split by double newlines or more
    paragraphs = re.split(r'\n\s*\n', text)
    return [p.strip() for p in paragraphs if p.strip()]

def paraphrase_text(sentence, num_variants=1):
    """Paraphrase a single sentence/paragraph"""
    if not sentence.strip():
        return ""
    
    # Format input untuk model
    text = f"paraphrase: {sentence} </s>"
    
    # Tokenize
    encoding = tokenizer(
        text, 
        padding='longest', 
        max_length=512,
        truncation=True,
        return_tensors="pt"
    )
    
    # Generate paraphrase
    with torch.no_grad():
        outputs = model.generate(
            input_ids=encoding["input_ids"],
            attention_mask=encoding["attention_mask"],
            max_length=512,
            do_sample=True,
            top_k=200,
            top_p=0.95,
            early_stopping=True,
            num_return_sequences=num_variants
        )
    
    # Decode hasil
    results = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    
    # Ambil hasil terbaik (yang pertama)
    return results[0] if results else sentence

def process_document(file, progress=gr.Progress()):
    """Process uploaded document"""
    if file is None:
        return None, "❌ Silakan upload file terlebih dahulu!"
    
    try:
        # Baca file
        progress(0, desc="Membaca file...")
        file_path = file.name
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            return None, "❌ File kosong!"
        
        # Split menjadi paragraphs
        progress(0.1, desc="Memproses paragraf...")
        paragraphs = split_into_paragraphs(content)
        total_paragraphs = len(paragraphs)
        
        if total_paragraphs == 0:
            return None, "❌ Tidak ada teks yang dapat diproses!"
        
        # Paraphrase setiap paragraph
        paraphrased_paragraphs = []
        for i, para in enumerate(paragraphs):
            progress((i + 1) / total_paragraphs, desc=f"Paraphrase paragraf {i+1}/{total_paragraphs}...")
            paraphrased = paraphrase_text(para)
            paraphrased_paragraphs.append(paraphrased)
        
        # Gabungkan kembali dengan double newline
        result = "\n\n".join(paraphrased_paragraphs)
        
        # Simpan hasil ke file temporary
        progress(1.0, desc="Menyimpan hasil...")
        output_filename = file_path.replace(".txt", "_paraphrased.txt").replace(".md", "_paraphrased.md")
        
        # Jika tidak ada extension, tambahkan _paraphrased.txt
        if not (output_filename.endswith("_paraphrased.txt") or output_filename.endswith("_paraphrased.md")):
            output_filename = output_filename + "_paraphrased.txt"
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(result)
        
        success_msg = f"✅ Berhasil! Diproses {total_paragraphs} paragraf."
        
        return output_filename, success_msg
        
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# Buat Gradio Interface
with gr.Blocks(title="Paraphrase Dokumen Indonesia") as demo:
    gr.Markdown(
        """
        # 📝 Paraphrase Dokumen Bahasa Indonesia
        
        Upload dokumen Anda (format .txt atau .md) dan dapatkan versi paraphrase-nya secara otomatis!
        
        **Model**: IndoT5-base-paraphrase - Model T5 khusus untuk paraphrase bahasa Indonesia
        """
    )
    
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="📄 Upload File (.txt atau .md)",
                file_types=[".txt", ".md"],
                type="filepath"
            )
            
            submit_btn = gr.Button("🚀 Paraphrase Dokumen", variant="primary", size="lg")
            
        with gr.Column():
            output_file = gr.File(label="📥 Download Hasil Paraphrase")
            status_text = gr.Textbox(label="Status", interactive=False, lines=2)
    
    gr.Markdown(
        """
        ---
        ### 💡 Tips:
        - Pastikan dokumen Anda dalam bahasa Indonesia
        - Proses akan memakan waktu tergantung panjang dokumen
        - Setiap paragraf akan di-paraphrase secara terpisah
        - Hasil terbaik untuk dokumen dengan paragraf yang jelas
        
        ### ⚠️ Limitasi:
        - Maksimal 512 token per paragraf
        - Kadang hasil paraphrase bisa mengandung informasi yang tidak ada di teks asli
        
        **Powered by**: [Wikidepia/IndoT5-base-paraphrase](https://huggingface.co/Wikidepia/IndoT5-base-paraphrase)
        """
    )
    
    # Event handler
    submit_btn.click(
        fn=process_document,
        inputs=[file_input],
        outputs=[output_file, status_text]
    )

# Launch app
if __name__ == "__main__":
    demo.launch()
