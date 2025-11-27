# 6. Information Architecture 🕸️

## 🗺️ Site Map

```
Home (/)
├── Header
│   ├── Logo
│   ├── Menu (Home, Blog, About)
│   └── CTA (Support Us)
├── Hero Section
│   ├── Headline (H1)
│   ├── Sub-headline
│   └── Tool Interface (The App)
│       ├── Tabs (Text | Document)
│       ├── Input Area / Dropzone
│       ├── Action Button (Paraphrase)
│       └── Output Area / Download
├── Features Section
│   ├── Why Us
│   └── How it Works
├── Ad Space (Middle)
├── FAQ Section (SEO Content)
└── Footer
    ├── Links (Privacy Policy, Terms, Contact)
    ├── Copyright
    └── Social Icons
```

## 🔄 User Flow Diagram

```mermaid
flowchart TD
    Start[User Lands on Site] --> Choice{Input Type?}
    
    Choice -- Text --> TextInput[Type/Paste Text]
    Choice -- File --> FileUpload[Upload .txt/.md]
    
    TextInput --> Validate[Check Length]
    FileUpload --> ValidateFile[Check Format/Size]
    
    Validate --> Process[Click Paraphrase]
    ValidateFile --> Process
    
    Process --> Loading[Show Progress & Ads]
    Loading --> API[Call Hono/HF API]
    API --> Result[Display Result]
    
    Result --> Actions{Next Action?}
    Actions -- Copy --> CopyText[Copy to Clipboard]
    Actions -- Download --> DownloadFile[Download File]
    Actions -- Retry --> Start
```

## 📂 Directory Structure (Monorepo)

```
indo-paraphrase/
├── apps/
│   ├── web/                 # React + Vite (Frontend)
│   │   ├── src/
│   │   │   ├── components/  # UI Components
│   │   │   ├── hooks/       # Custom Hooks
│   │   │   └── pages/       # Route Pages
│   │   └── public/
│   └── api/                 # Hono (Backend Worker)
│       ├── src/
│       │   └── index.ts     # API Routes
│       └── wrangler.toml    # Cloudflare Config
├── packages/
│   └── ui/                  # Shared UI (Optional)
├── docs/                    # Documentation (This folder)
├── package.json             # Root Config
└── turbo.json              # Turborepo Config (Optional)
```
