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
2. **Immediate Action**: Giant textarea langsung di landing, no scroll needed - user langsung bisa paste dan go.
3. **Smart Flow**: 
   - User paste text/ketik → klik "Paraphrase" 
   - **Hasil muncul semua paragraph** (auto-paraphrased)
   - User bisa **pilih paragraph tertentu** untuk di-paraphrase ulang (iterative improvement)
4. **Save for Later**: Untuk dokumen panjang, user bisa login (Google OAuth) dan save draft sampai 5x.
5. **Rate Limiting (Comprehensive & Smart)**:
   
   **Free Tier (No Login)**:
   - Max 10 paragraf per dokumen
   - Max 200 kata (atau ~1000 karakter) per paragraf
   - Max 2000 kata total per dokumen
   - Max 5 dokumen per jam per IP
   - Max 20 dokumen per hari per IP
   - Cooldown 10 menit setelah mencapai limit harian
   
   **Login Tier (Google OAuth)**:
   - Max 20 paragraf per dokumen
   - Max 400 kata (atau ~2000 karakter) per paragraf
   - Max 5000 kata total per dokumen  
   - Max 10 dokumen per jam per user
   - Max 50 dokumen per hari per user
   - No cooldown (reset langsung jam berikutnya)
   
   **"Pay with Exposure" Bonus**:
   - Review Google Play/App Store → +10 dokumen instant
   - Share ke Twitter/Facebook (verified) → +5 dokumen per share (max 2x/hari)
   - Total bonus max: +20 dokumen per hari
   
   **Protection Mechanisms**:
   - Auto-split paragraf >200 kata (free) atau >400 kata (login) menjadi chunks
   - Rate limit by IP + browser fingerprint (prevent VPN abuse)
   - Suspicious pattern detection (same text repeated, bot-like behavior) → ban 24h
6. **Free & Ad-Supported**: Gratis digunakan (freetier), monetisasi via iklan (AdSense) yang agresif tapi tidak merusak UX.
7. **Modern Tech Stack**: Astro (SEO optimal) + Cloudflare (fast edge delivery).

## 🌟 Unique Selling Points (USP)
- **Iterative Paraphrase** - Hasil langsung muncul, lalu user bisa pilih paragraph mana yang mau di-improve lagi.
- **Pay with Exposure** - Review & share = dapat quota tambahan (win-win marketing).
- **Save Draft** - Login Google untuk save progress (max 5 drafts).
- **Immediate Action UI** - Textarea giant di atas fold, langsung action.
- **100% Gratis & Tanpa Login** (untuk fitur paraphrase dasar).
- **Fair Limits (Multi-Layer Protection)**: 
  - **Free**: 10 para/doc (max 200 kata/para), 5 doc/jam, 20 doc/hari per IP
  - **Login**: 20 para/doc (max 400 kata/para), 10 doc/jam, 50 doc/hari
  - **Exposure Bonus**: Review app (+10 doc), Share sosmed (+5 doc/share, max 2x/hari)
  - **Anti-Abuse**: Auto-chunk paragraf panjang, fingerprint tracking, bot detection
- **Infrastruktur Cepat** (Cloudflare Edge).
- **Privasi**: Dokumen tidak disimpan permanen (processed on-the-fly), kecuali user opt-in save draft.

## 💰 Monetization Ideas
1. **Aggressive Display Ads**: Banner iklan di segala sisi (Top, Bottom, Sidebar).
2. **Native Ads**: Iklan yang menyatu dengan konten.
3. **Interstitial Ads**: Iklan layar penuh sebelum download file.
4. **Donation/Support**: "Traktir Kopi" button.

## 🚀 Growth Loops
- **SEO Strategy**: Target keyword "paraphrase online indonesia", "cek plagiarisme gratis", "ubah kalimat online".
- **Viral Loop**: Share hasil unik ke sosmed (Twitter/X thread generator).
