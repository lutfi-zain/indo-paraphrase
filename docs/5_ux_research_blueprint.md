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

### Color Palette
- **Primary**: `Blue-600` (#2563eb) - Trust, Tech, Professional.
- **Secondary**: `Emerald-500` (#10b981) - Success, Safe, Correct.
- **Background**: `Slate-50` (#f8fafc) - Clean, Readability.
- **Text**: `Slate-900` (#0f172a) - High Contrast.

### Typography
- **Font**: `Inter` atau `Plus Jakarta Sans` (Modern, Readable, Google Fonts).

### UI Components
- **Card**: White bg, soft shadow, rounded-xl.
- **Button**: Pill shape, gradient hover effect.
- **Input Area**: Minimalist border, focus ring.
