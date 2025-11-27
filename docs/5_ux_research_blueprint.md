# 5. UX Research & Blueprint 🎨

## ⚡ Critical User Feedback (Real Users)

### Feedback Summary
1. **"Langsung action, no fluff"**: User wants immediate access to paraphrase tool on landing (paste/type), tidak perlu scroll atau baca dulu.
2. **"Save for later"**: Untuk teks panjang, user butuh fitur save progress (requires account/login).
3. **"Selective paraphrase"**: User mau bisa **klik bagian tertentu** untuk di-paraphrase, bukan seluruh dokumen sekaligus.

### Design Implications
- ❌ **Remove**: Hero section dengan marketing copy panjang.
- ✅ **Add**: Giant textarea langsung di atas fold dengan placeholder "Paste teks Anda di sini...".
- ✅ **Add**: Authentication system (Google OAuth simple).
- ✅ **Add**: Interactive text editor dengan highlight & click-to-paraphrase per paragraph.

## 👥 User Personas

### 1. Budi si Mahasiswa (The Deadline Fighter)
- **Umur**: 21 Tahun.
- **Goal**: Lolos cek Turnitin untuk skripsi bab 2.
- **Pain Point**: Otak buntu, kalimat skripsi kaku, takut plagiat.
- **Behavior**: Cari tool gratisan, gak mau ribet login, internet pas-pasan.
- **Needs**: Cepat, Gratis, Hasil terlihat akademis.

### 2. Sari si Content Writer (The Volume Creator)
- **Umur**: 25 Tahun.
- **Goal**: Rewrite 10 artikel berita per hari.
- **Pain Point**: Capek mikir variasi kalimat yang sama berulang-ulang.
- **Behavior**: Pakai laptop, multitasking banyak tab.
- **Needs**: Bulk processing, Copy-paste cepat.

## 🗺️ User Journey Map

### Scenario: Paraphrase Dokumen Skripsi
1. **Discovery**: Search Google "paraphrase dokumen indonesia gratis". Klik link IndoParaphrase.
2. **Onboarding**: Masuk landing page. Langsung paham fungsi dari headline "Paraphrase Dokumen Bahasa Indonesia Gratis".
3. **Action**: Drag file `bab2_skripsi.txt` ke kotak upload.
4. **Waiting**: Melihat progress bar berjalan "Memproses paragraf 1/10...". (Kesempatan lihat iklan).
5. **Result**: Hasil muncul. Budi baca sekilas paragraf pertama. "Wah oke nih".
6. **Conversion**: Klik tombol "Download Hasil".
7. **Retention**: Bookmark halaman untuk Bab 3 besok.

## 🎨 Design System (Brief)

### Design Goals
- **Professional-Grade**: Terlihat seperti SaaS product yang worth $$/month, bukan tool gratisan asal jadi.
- **Freemium Teaser**: Show locked features dengan badge "🔒 Login untuk Save Draft" → create desire to upgrade.
- **Trust Signals**: Tampilkan user count, paragraphs processed today, testimonials (even if mock at start).

### Color Palette
- **Primary**: `Blue-600` (#2563eb) - Trust, Tech, Professional.
- **Accent**: `Emerald-500` (#10b981) - Success, Action, "Go".
- **Premium**: `Purple-600` (#9333ea) - Exclusive, Upgrade, Premium features.
- **Background**: `Slate-50` (#f8fafc) - Clean, Modern, Premium feel.
- **Text**: `Slate-900` (#0f172a) - High Contrast, Readable.

### Typography
- **Font**: `Inter` atau `Plus Jakarta Sans` (Modern, Professional).
- **Hierarchy**:
  - H1: 48px, Bold (Landing CTA)
  - H2: 32px, SemiBold (Section headers)
  - Body: 16px, Regular (Readable)
  - Small: 14px (Meta info, ads disclaimer)

### UI Components
- **Card**: White bg, subtle shadow `shadow-lg`, rounded-xl, border `border-gray-200`.
- **Button Primary**: Gradient `from-blue-600 to-blue-700`, bold text, `shadow-md hover:shadow-xl`.
- **Button Premium**: Gradient `from-purple-600 to-purple-700` with sparkle icon ✨.
- **Input Area**: Clean border, smooth focus ring, placeholder with helpful hint.
- **Premium Badge**: Small pill badge `🔒 Login` with purple bg, white text.

### Freemium "Intip" Strategy
Show locked features prominently dengan value prop:

**Example UI Card** (Visible to all users):
```
┌─────────────────────────────────────┐
│ 💾 Save Draft                  🔒   │
│ ───────────────────────────────────  │
│ Simpan progress untuk lanjut nanti   │
│ • Sampai 5 draft                     │
│ • Auto-save setiap 30 detik          │
│ • Akses dari device mana pun         │
│                                      │
│ [🔓 Login dengan Google - Gratis]   │
└─────────────────────────────────────┘
```

**History Panel** (Grayed out if not logged in):
```
┌─────────────────────────────────────┐
│ 📜 History (Last 10)           🔒   │
│ ───────────────────────────────────  │
│ (blur effect + overlay)              │
│   "Login untuk lihat riwayat Anda"   │
│                                      │
│ [Login untuk Akses]                 │
└─────────────────────────────────────┘
```
