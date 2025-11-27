# 4. Business & Product Spec 📝

## 🏗️ Technical Architecture (Cloudflare Monorepo)

### Stack
- **Frontend**: React + Vite + TailwindCSS (Deployed di Cloudflare Pages).
- **Backend (BFF)**: Hono.js (Deployed di Cloudflare Workers).
- **AI Engine**: HuggingFace Spaces (Existing Gradio API).
- **Database (Optional)**: Cloudflare D1 (untuk simpan log/feedback user, bukan konten dokumen).

### Architecture Diagram
```mermaid
graph LR
    User[User Browser] -- HTTPS --> CF[Cloudflare Pages (React)]
    CF -- API Req --> Worker[Hono Worker (BFF)]
    Worker -- Inference Req --> HF[HuggingFace Space (IndoT5)]
    HF -- Result --> Worker
    Worker -- JSON --> CF
    CF -- Render --> User
```

## 📱 Product Features (MVP)

### P0 (Must Have - Launch)
1. **Landing Page SEO Friendly**: H1, Meta Tags, Content rich keywords.
2. **File Uploader**: Drag & drop area (.txt, .md).
3. **Text Input**: Textarea untuk copy-paste manual (max 5000 chars).
4. **Paraphrase Engine**: Integrasi ke HF Space API.
5. **Result Viewer**: Side-by-side comparison (Original vs Paraphrased).
6. **Copy/Download**: Tombol copy teks dan download file hasil.
7. **AdSense Slots**: Placeholder untuk iklan (Top Banner, Sidebar, Bottom).

### P1 (Nice to Have - Next Update)
1. **History**: Simpan 5 riwayat terakhir di LocalStorage.
2. **Feedback Loop**: Tombol Like/Dislike untuk fine-tuning model kedepannya.
3. **Dark Mode**: Toggle tema.

## 💰 Monetization Strategy Implementation

### Ad Placements
1. **Top Leaderboard (728x90)**: Di atas header, terlihat pertama kali.
2. **Sidebar (300x250)**: Di sebelah kanan input area (desktop only).
3. **In-Feed/Native**: Di antara input box dan result box (mobile friendly).
4. **Download Interstitial (Optional)**: Tampilkan iklan modal saat klik download (high value).

### SEO Strategy for Traffic
- **Keywords**: "paraphrase indonesia", "cek plagiat gratis", "rewrite artikel", "bot nulis".
- **Blog Section**: Buat artikel tips menulis skripsi/artikel di sub-folder `/blog` (support by Cloudflare Pages).

## 📅 Roadmap
- **Week 1**: Setup Monorepo, Porting UI Gradio ke React, Integrasi Hono -> HF.
- **Week 2**: Polish UI/UX, SEO Optimization, Daftar AdSense.
- **Week 3**: Launch & Share ke komunitas.
