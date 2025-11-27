# Indo-Paraphrase Monorepo

Web app untuk paraphrase dokumen bahasa Indonesia dengan monetisasi iklan.

## 📁 Structure

```
indo-paraphrase/
├── apps/
│   ├── web/          # Astro frontend (Cloudflare Pages)
│   └── api/          # Hono backend (Cloudflare Workers)
├── docs/             # Business & product documentation
└── README.md
```

## 🚀 Development

### Frontend (Astro)
```bash
cd apps/web
npm install
npm run dev
```

### Backend (Hono)
```bash
cd apps/api
npm install
npm run dev
```

## 🌐 Deployment

### Frontend to Cloudflare Pages
```bash
cd apps/web
npm run build
wrangler pages deploy dist
```

### Backend to Cloudflare Workers
```bash
cd apps/api
npm run deploy
```

### Setup D1 Database
```bash
cd apps/api
wrangler d1 create paraphrase_db
wrangler d1 execute paraphrase_db --file=schema.sql
```

Update `wrangler.toml` with your D1 database ID.

## ⚙️ Environment Variables

### API (wrangler.toml)
- `GOOGLE_CLIENT_ID`: Your Google OAuth client ID
- `HUGGINGFACE_API_URL`: HuggingFace Space API endpoint

## 📚 Documentation

See `/docs` folder for:
- Business strategy
- UX research
- Technical specs
- Monetization strategy

## 🎯 Features

- ✅ Selective paragraph paraphrase
- ✅ Google OAuth authentication
- ✅ Save drafts (max 5 per user)
- ✅ SEO optimized (Astro SSG)
- ✅ Aggressive ad monetization
- ✅ Cloudflare Edge deployment
