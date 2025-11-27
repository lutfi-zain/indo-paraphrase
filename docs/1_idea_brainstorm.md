# 1. Idea Brainstorm Kit 💡

## 🎯 Core Concept
**Nama Produk**: IndoParaphrase (Working Title)
**Tagline**: "Paraphrase Dokumen Bahasa Indonesia, Gratis & Cepat"
**Elevator Pitch**: Web app gratis untuk menulis ulang (paraphrase) teks dan dokumen bahasa Indonesia agar lebih unik, formal, atau santai, tanpa ribet login, didukung oleh AI canggih.

## 🧠 The "Why" (Masalah)
1. **Plagiarisme**: Mahasiswa/penulis takut terkena deteksi plagiarisme (Turnitin, dll).
2. **Writer's Block**: Bingung mencari padanan kata atau menyusun kalimat ulang.
3. **Keterbatasan Tool**: Tool paraphrase bagus kebanyakan bahasa Inggris (Quillbot), yang bahasa Indonesia seringkali kaku/bayar mahal.
4. **Format Dokumen**: Copy-paste teks panjang itu capek, user butuh upload file langsung jadi.

## 💡 The "Solution" (Solusi)
1. **Native Indonesian AI**: Menggunakan model IndoT5 yang dilatih khusus bahasa Indonesia.
2. **Document First**: Fokus pada upload file (.txt, .md, future: .docx, .pdf) -> proses -> download.
3. **Free & Ad-Supported**: Gratis digunakan (freetier), monetisasi via iklan (AdSense) yang tidak mengganggu.
4. **Modern UX**: Interface cepat, bersih, berbasis React + Vite di Cloudflare.

## 🌟 Unique Selling Points (USP)
- **100% Gratis & Tanpa Login** (untuk fitur dasar).
- **Support Dokumen Panjang** (via paragraph splitting).
- **Infrastruktur Cepat** (Cloudflare Edge).
- **Privasi**: Dokumen tidak disimpan permanen (processed on-the-fly).

## 💰 Monetization Ideas
1. **Display Ads**: Banner iklan di samping/bawah hasil paraphrase.
2. **Native Ads**: Iklan yang menyatu dengan konten (misal: rekomendasi tool grammar).
3. **Donation/Support**: "Traktir Kopi" button.
4. **Premium (Future)**: Hapus iklan, prioritas antrian, support .docx/.pdf, mode "Formal/Santai".

## 🚀 Growth Loops
- **Watermark (Soft)**: "Paraphrased by IndoParaphrase" di footer file hasil (bisa dihapus user, tapi default ada).
- **SEO Strategy**: Target keyword "paraphrase online indonesia", "cek plagiarisme gratis", "ubah kalimat online".
- **Viral Loop**: Share hasil unik ke sosmed (Twitter/X thread generator).
