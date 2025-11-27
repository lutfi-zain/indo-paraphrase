# 📝 Paraphrase Dokumen Bahasa Indonesia

Web application untuk melakukan paraphrase dokumen bahasa Indonesia secara otomatis menggunakan model **IndoT5-base-paraphrase**.

## ✨ Fitur

- 📄 Upload dokumen format `.txt` atau `.md`
- 🤖 Paraphrase otomatis menggunakan model T5 khusus bahasa Indonesia
- 📊 Progress tracking untuk dokumen panjang
- 💾 Download hasil paraphrase
- 🎨 Interface yang user-friendly dengan Gradio

## 🚀 Cara Menggunakan (Lokal)

### Prerequisites

- Python 3.8 atau lebih baru
- pip

### Instalasi

1. Clone repository ini:
```bash
git clone <repository-url>
cd indo-paraphrase
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
python app.py
```

4. Buka browser dan akses URL yang muncul di terminal (biasanya `http://127.0.0.1:7860`)

## 🌐 Deploy ke HuggingFace Spaces (GRATIS!)

### Cara Deploy:

1. **Buat akun HuggingFace** (jika belum punya):
   - Kunjungi [huggingface.co](https://huggingface.co) dan sign up

2. **Buat Space baru**:
   - Klik profil → "New Space"
   - Pilih nama untuk Space Anda
   - Pilih SDK: **Gradio**
   - Pilih Hardware: **CPU Basic** (gratis)
   - Klik "Create Space"

3. **Upload files**:
   - Upload file-file berikut ke Space Anda:
     - `app.py`
     - `requirements.txt`
     - `README.md` (opsional)
   
   Atau gunakan Git:
   ```bash
   git clone https://huggingface.co/spaces/USERNAME/SPACENAME
   cd SPACENAME
   cp /path/to/indo-paraphrase/app.py .
   cp /path/to/indo-paraphrase/requirements.txt .
   git add .
   git commit -m "Initial commit"
   git push
   ```

4. **Tunggu build selesai** (~2-3 menit)

5. **Aplikasi sudah live!** 🎉

URL aplikasi Anda: `https://huggingface.co/spaces/USERNAME/SPACENAME`

## 📖 Cara Penggunaan

1. Klik tombol "Upload File" dan pilih dokumen `.txt` atau `.md` Anda
2. Klik tombol "🚀 Paraphrase Dokumen"
3. Tunggu proses selesai (akan ada progress bar)
4. Download hasil paraphrase dengan klik file yang muncul

## ⚙️ Cara Kerja

Aplikasi ini:
1. Membaca file yang di-upload
2. Memisahkan dokumen menjadi paragraf-paragraf
3. Melakukan paraphrase untuk setiap paragraf menggunakan model IndoT5
4. Menggabungkan kembali hasil paraphrase
5. Menyediakan file hasil untuk di-download

## ⚠️ Limitasi

- Model memiliki batas 512 token per paragraf
- Kadang hasil paraphrase mengandung informasi yang tidak ada di teks asli (hallucination)
- Kualitas terbaik untuk teks formal bahasa Indonesia

## 🔧 Teknologi yang Digunakan

- **[Gradio](https://gradio.app/)** - Web interface
- **[Transformers](https://huggingface.co/docs/transformers)** - Model inference
- **[PyTorch](https://pytorch.org/)** - Deep learning framework
- **[IndoT5-base-paraphrase](https://huggingface.co/Wikidepia/IndoT5-base-paraphrase)** - Pretrained model

## 📝 Contoh

**Input**:
```
Anak anak melakukan piket kelas agar kebersihan kelas terjaga.
Mereka sangat senang membantu guru.
```

**Output** (contoh):
```
Para siswa melaksanakan piket di kelas supaya kelas tetap bersih.
Mereka dengan gembira membantu tenaga pengajar.
```

## 🙏 Credits

- Model oleh [Wikidepia](https://huggingface.co/Wikidepia)
- Trained on translated PAWS dataset
- Thanks to Tensorflow Research Cloud for TPU support

## 📄 License

MIT License - Silakan digunakan secara bebas!

## 🤝 Kontribusi

Kontribusi sangat welcome! Silakan buat PR atau issue untuk improvement.

---

**Made with ❤️ for Indonesian NLP Community**
