# 3. Validation Kit ✅

## 🧪 Hypotheses to Test
1. **Problem**: Orang butuh paraphrase *dokumen* langsung, bukan cuma copy-paste teks.
2. **Solution**: Hasil model IndoT5 cukup bagus untuk standar akademik/formal.
3. **Monetization**: User tidak keberatan dengan iklan asalkan tool gratis.

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
