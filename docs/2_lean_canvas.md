# 2. Lean Canvas 📊

| Problem (Masalah) | Solution (Solusi) | Unique Value Proposition (UVP) | Unfair Advantage | Customer Segments |
| :--- | :--- | :--- | :--- | :--- |
| 1. Mahasiswa takut plagiarisme.<br>2. Penulis konten butuh variasi kalimat.<br>3. Tool paraphrase Indo yang ada mahal/kaku.<br>4. Ribet copy-paste teks panjang. | 1. AI Paraphraser Bahasa Indonesia.<br>2. Support upload dokumen (.txt, .md).<br>3. Gratis dengan model iklan.<br>4. UI/UX modern & cepat. | **"Satu-satunya tool paraphrase dokumen Bahasa Indonesia yang Gratis, Cepat, dan Tanpa Login."** | 1. Menggunakan Model Open Source (IndoT5) yang di-hosting sendiri (cost control).<br>2. Infrastruktur Cloudflare (Low Latency).<br>3. Fokus niche Bahasa Indonesia. | 1. **Mahasiswa** (Skripsi, Tugas).<br>2. **Content Writer/Blogger** (Rewrite artikel).<br>3. **Jurnalis**.<br>4. **Akademisi/Dosen**. |
| **Existing Alternatives** | **Key Metrics** | **High-Level Concept** | **Channels** | **Early Adopters** |
| 1. Quillbot (Bayar/Limit).<br>2. Google Translate (Bolak-balik).<br>3. Jasa Paraphrase Manual (Mahal).<br>4. Smodin (Limit ketat). | 1. Daily Active Users (DAU).<br>2. Number of Documents Processed.<br>3. Ad Impressions/Clicks.<br>4. Bounce Rate. | "Quillbot versi Indonesia yang Gratis & Support Dokumen." | 1. SEO (Search Engine).<br>2. TikTok/Reels (Tips Skripsi).<br>3. Twitter/X (Utas produktivitas).<br>4. Grup Telegram/WA Mahasiswa. | Mahasiswa tingkat akhir yang sedang mengejar deadline skripsi/jurnal. |

## 💰 Cost Structure
1. **Hosting**: Cloudflare Pages/Workers (Free Tier cukup besar, scale murah).
2. **Model Inference**: HuggingFace Spaces (Free Tier CPU) atau upgrade ke GPU ($0.60/hr) jika trafik meledak (bisa cover pakai iklan).
3. **Domain**: ~Rp 150rb/tahun.

## 💵 Revenue Streams
1. **Google AdSense**: Estimasi RPM Rp 5.000 - Rp 15.000 (tergantung niche pendidikan).
2. **Affiliate**: Rekomendasi tool cek plagiarisme berbayar (misal Turnitin check service).
