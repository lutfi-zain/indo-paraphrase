# 4. Business & Product Spec 📝

## 🏗️ Technical Architecture (Cloudflare Monorepo)

### Stack (SEO Optimized)
- **Frontend**: **Astro** (SSG/SSR) + React (Islands Architecture).
  - *Why Astro?* Performa HTML statis maksimal untuk SEO, tapi tetap bisa pakai React untuk komponen interaktif (uploader/paraphraser).
- **Styling**: TailwindCSS.
- **Backend (BFF)**: Hono.js (Deployed di Cloudflare Workers).
- **AI Engine**: HuggingFace Spaces (Existing Gradio API).

### Architecture Diagram
```mermaid
graph LR
    User[User Browser] -- HTTPS --> CF[Cloudflare Pages (Astro)]
    CF -- API Req --> Worker[Hono Worker (BFF)]
    Worker -- Inference Req --> HF[HuggingFace Space (IndoT5)]
    HF -- Result --> Worker
    Worker -- JSON --> CF
    CF -- Render --> User
```

## 📱 Product Features (MVP) - Updated Based on User Feedback

### P0 (Must Have - Launch)
1. **Immediate Action UI**: 
   - Giant textarea langsung di hero section (no scroll needed).
   - Placeholder: "Paste atau ketik teks Anda di sini untuk paraphrase...".
   - Instant action button visible.

2. **Selective Paraphrase**:
   - Setelah paste, teks otomatis di-split per paragraph.
   - Each paragraph dapat di-klik untuk select/deselect.
   - Tombol "Paraphrase Selected" hanya memproses yang dipilih.
   - UI: Checkbox per paragraph atau highlight on click.

3. **Authentication (Google OAuth)**:
   - Login button di top-right corner.
   - Untuk fitur "Save for Later" (drafts).

4. **Save for Later**:
   - Jika user login, bisa save current state (original text + selected paragraphs).
   - Database: Cloudflare D1 (store user_id, document_text, timestamp).
   - Max 5 saved drafts per user (free tier).

5. **Download System**: Interstitial ad page before download.

6. **AdSense Slots**: As per aggressive strategy.

## 💰 Monetization Strategy Implementation (High Density)

### Ad Placements ("The Porn Site Strategy" - Clean Version)
Target: Maximize Viewability & Clicks tanpa merusak fungsi utama.

1. **Sticky Top Leaderboard (728x90)**: Selalu nempel di atas layar.
2. **Sticky Bottom Anchor (320x50 / 728x90)**: Selalu nempel di bawah layar (Mobile & Desktop).
3. **Double SkyScraper (160x600)**: Kiri DAN Kanan konten utama (Desktop only).
4. **Native In-Feed**: Di antara kotak Input dan Output.
5. **Interstitial Page**: Saat klik "Download", user diarahkan ke halaman khusus (tunggu 5 detik) yang isinya iklan besar (300x250 atau 336x280) sebelum file terunduh.
6. **Pop-under (Optional)**: Jika revenue kurang, aktifkan pop-under 1x per 24 jam per user (hati-hati UX).

### SEO Strategy for Traffic
- **Tech**: Astro menjamin HTML murni ter-render di server (bukan client-side rendering kosong ala React SPA biasa).
- **Keywords**: "paraphrase indonesia", "cek plagiat gratis", "rewrite artikel", "bot nulis".
- **Blog Section**: `/blog` menggunakan Astro Content Collections (Markdown) untuk artikel tips skripsi.

## 📅 Roadmap
- **Week 1**: Setup Monorepo, Porting UI Gradio ke React, Integrasi Hono -> HF.
- **Week 2**: Polish UI/UX, SEO Optimization, Daftar AdSense.
- **Week 3**: Launch & Share ke komunitas.
