# 3. Validation Kit ✅

## 🧪 Hypotheses to Test

### ✅ VALIDATED (From Real Users)
1. ~~**Problem**: Orang butuh paraphrase *dokumen* langsung~~ → **PIVOT**: User mau **pilih paragraph**, bukan full doc.
2. ~~Full landing page with marketing copy~~ → **REJECTED**: User mau immediate action, no fluff.
3. **NEW**: User butuh save draft untuk teks panjang (requires auth).

### 🔍 STILL TO VALIDATE
1. **Solution**: Hasil model IndoT5 cukup bagus untuk standar akademik/formal.
2. **Monetization**: User tidak keberatan dengan iklan agresif asalkan tool gratis.

## 🔍 Validation Experiments

### Experiment 1: "The Smoke Test" (Landing Page)
- **Goal**: Cek demand via SEO/Traffic.
- **Action**: Deploy landing page di Cloudflare dengan tombol "Upload Dokumen".
- **Metric**: Click Rate pada tombol upload.
- **Success Criteria**: >100 klik/hari dalam minggu pertama launch.

### Experiment 2: "Quality Check" (User Feedback)
- **Goal**: Validasi kualitas AI.
- **Action**: Tambahkan tombol "👍/👎" di setiap hasil paraphrase.
- **Metric**: Ratio Like vs Dislike.
- **Success Criteria**: >70% Positive Feedback.

### Experiment 3: "Ad Tolerance"
- **Goal**: Cek apakah iklan mengganggu retention.
- **Action**: Pasang 1 banner iklan.
- **Metric**: Bounce rate & Time on Site.
- **Success Criteria**: Bounce rate <60%.

## ✅ Real User Feedback (Received)

**Date**: Nov 2024
**Sample Size**: Small focus group (early users)

### Key Findings:
1. **"Langsung action, no fluff"** (100% agreement)
   - Users want immediate access to textarea
   - Marketing copy di hero section = ignored/annoying
   - **Action Taken**: Removed hero marketing, giant textarea di atas fold

2. **"Save for later"** (80% requested)
   - Untuk teks panjang (>1000 words), users want to save progress
   - Willing to login if it means saving work
   - **Action Taken**: Implemented Google OAuth + D1 draft storage (max 5)

3. **"Selective paraphrase"** (90% prefer)
   - Users don't want full-doc paraphrase
   - Want to click specific paragraphs only
   - Saves time & lets them keep good paragraphs unchanged
   - **Action Taken**: Built 3-stage flow (input → select → result)

## 📋 Interview Questions (untuk User Test)
1. "Biasanya pakai tool apa buat paraphrase?"
2. "Apa yang paling nyebelin dari tool yang sekarang dipakai?"
3. "Kalau ada tool gratis tapi ada iklannya, keberatan nggak?"
4. "Lebih sering copy-paste teks atau upload file?"

## 📊 Competitor Analysis Matrix
| Feature | IndoParaphrase (Us) | Quillbot | Google Translate (Trick) | Jasa Manual |
| :--- | :--- | :--- | :--- | :--- |
| **Bahasa** | Spesialis Indo | Multi (Indo kurang natural) | Multi (Kacau grammar) | Indo Bagus |
| **Harga** | **Gratis** | Freemium ($$) | Gratis | Mahal ($$$) |
| **Dokumen** | **Yes (.txt, .md)** | Premium Only | Document Translation Only | Yes |
| **Kecepatan** | Cepat (Automated) | Cepat | Cepat | Lambat (Hari) |
