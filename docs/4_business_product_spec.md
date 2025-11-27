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

## 📱 Product Features (MVP)

### P0 (Must Have - Launch)
1. **Landing Page SEO Friendly**: Astro SSG untuk load speed 100/100 di Lighthouse.
2. **File Uploader**: Drag & drop area (.txt, .md).
3. **Paraphrase Engine**: Integrasi ke HF Space API.
4. **Result Viewer**: Side-by-side comparison.
5. **Download System**: Dengan halaman interstitial (iklan dulu baru download).
6. **AdSense Slots**: Placeholder untuk iklan agresif.

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
