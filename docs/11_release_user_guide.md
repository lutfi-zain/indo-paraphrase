# 11. Release & User Guide 🚀

## 📦 Deployment Guide

### Prerequisites
- Node.js 18+
- npm or pnpm
- Wrangler CLI
- Cloudflare account
- Google OAuth credentials

---

## 🚀 Production Deployment

### Step 1: Setup Cloudflare Account
1. Sign up at [cloudflare.com](https://cloudflare.com)
2. Create new project
3. Note your Account ID

### Step 2: Create D1 Database
```bash
cd apps/api
wrangler d1 create paraphrase_db
```

Copy the database ID and update `wrangler.toml`:
```toml
[[d1_databases]]
binding = "DB"
database_name = "paraphrase_db"
database_id = "YOUR_DATABASE_ID_HERE"
```

### Step 3: Initialize Database Schema
```bash
wrangler d1 execute paraphrase_db --file=schema.sql
```

### Step 4: Setup Google OAuth
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create new project: "IndoParaphrase"
3. Enable Google+ API
4. Create OAuth 2.0 credentials:
   - Authorized origins: `https://indoparaphrase.com`
   - Authorized redirect: `https://indoparaphrase.com/auth/callback`
5. Copy Client ID & Secret

Update `wrangler.toml`:
```toml
[vars]
GOOGLE_CLIENT_ID = "your-client-id"
HUGGINGFACE_API_URL = "https://0xbujang-indonesia-paraphrase.hf.space/api/predict"
```

Add secret:
```bash
wrangler secret put GOOGLE_CLIENT_SECRET
# Paste your secret when prompted
```

### Step 5: Deploy API (Workers)
```bash
cd apps/api
npm install
npm run deploy
```

Note the deployed URL: `https://indo-paraphrase-api.workers.dev`

### Step 6: Deploy Frontend (Pages)
```bash
cd apps/web
npm install
npm run build
wrangler pages deploy dist --project-name=indoparaphrase
```

Your site will be live at: `https://indoparaphrase.pages.dev`

### Step 7: Connect Custom Domain
1. In Cloudflare dashboard → Pages → indoparaphrase
2. Click "Custom domains"
3. Add `indoparaphrase.com`
4. Update DNS (auto-configured by Cloudflare)

---

## 🔧 Configuration Checklist

Before going live, verify:
- [ ] D1 database created & schema applied
- [ ] Google OAuth credentials configured
- [ ] HuggingFace API URL correct
- [ ] Environment variables set
- [ ] Custom domain connected
- [ ] SSL certificate active (Cloudflare auto)
- [ ] AdSense code added (update publisher ID)
- [ ] Analytics tracking code added

---

## 👥 User Guide

### For Free Users

#### How to Paraphrase Text
1. **Visit** [indoparaphrase.com](https://indoparaphrase.com)
2. **Paste** your Indonesian text (up to 2000 words)
3. **Click** "Paraphrase" button
4. **Wait** 2-3 seconds for results
5. **Review** the paraphrased text
6. **Select** specific paragraphs to re-paraphrase (optional)
7. **Download** or copy the final result

#### Rate Limits (Free)
- 10 paragraphs per document
- Max 200 words per paragraph
- 5 documents per hour
- 20 documents per day

---

### For Logged-In Users

#### How to Login
1. Click "**Login with Google**" button (top-right)
2. Select your Google account
3. Grant permissions
4. You're now logged in!

#### Benefits of Login
- ✅ **2x Quota**: 20 paragraphs/doc, 50 docs/day
- ✅ **Save Drafts**: Up to 5 saved documents
- ✅ **History**: See your last 10 paraphrased texts
- ✅ **Auto-save**: Progress saved every 30 seconds
- ✅ **No Cooldown**: Instant reset every hour

#### How to Save a Draft
1. Paste your text
2. Click "Paraphrase"
3. Click "💾 Save Draft" button
4. Name your draft (optional)
5. Draft saved in sidebar

#### How to Load a Draft
1. Login to your account
2. Open "Your Drafts" sidebar (left side)
3. Click on any draft
4. Content loads into editor
5. Continue editing

---

### How to Earn Bonus Quota

#### Option 1: Share to Twitter (+5 docs)
1. Click "Share to Twitter" button
2. Post the auto-generated tweet
3. Wait 5 seconds for verification
4. Bonus added automatically
Limit: 2x per week

#### Option 2: Invite Friends (+2 docs/signup)
1. Copy your referral link (in profile)
2. Share to friends via WA/Telegram
3. When they sign up → you get +2 docs
Limit: 50 docs/month

#### Option 3: Weekly Contest (Win unlimited!)
1. Post your before-after result
2. Use hashtag #IndoParaphraseChallenge
3. Top 10 most-liked → 1 week unlimited access

---

## ❓ FAQ

**Q: Apakah dokumen saya disimpan?**
A: Tidak. Dokumen di-process on-the-fly dan langsung dihapus. Kecuali Anda login dan klik "Save Draft".

**Q: Bisa paraphrase bahasa Inggris?**
A: Tidak. Tool ini khusus Bahasa Indonesia. Untuk Inggris pakai Quillbot.

**Q: Kenapa hasil kadang aneh?**
A: AI masih belajar. Coba klik paragraph tersebut dan "Rephrase" lagi untuk hasil lebih baik.

**Q: Limit per jam itu reset jam berapa?**
A: Reset setiap jam sharp. Misal Anda pakai jam 10:30, reset jam 11:00.

**Q: Bisa bayar untuk unlimited?**
A: Belum. Fitur premium sedang dalam development (Q2 2025).

---

## 🆘 Troubleshooting

### Issue: "Hourly limit reached"
**Solution**: Wait until top of next hour, or login to get 2x quota.

### Issue: Paraphrase button not working
**Solution**: 
1. Check your internet connection
2. Refresh the page
3. Clear browser cache
4. Try different browser

### Issue: Login tidak bisa
**Solution**:
1. Check if popup blocker enabled (disable it)
2. Try incognito mode
3. Clear cookies for the site

### Issue: Draft tidak tersimpan
**Solution**:
1. Pastikan Anda sudah login
2. Check internet connection
3. Max 5 drafts (hapus draft lama)

---

## 📞 Support

**Email**: support@indoparaphrase.com
**Twitter**: [@IndoParaphrase](https://twitter.com/IndoParaphrase)
**Response time**: <24 hours
