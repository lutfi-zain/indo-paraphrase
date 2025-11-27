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

## 🔄 User Flow Diagram (Updated with Selective Paraphrase)

```mermaid
flowchart TD
    Start[User Lands on Site] --> DirectPaste[Giant Textarea Visible]
    
    DirectPaste --> Input{Input Method?}
    Input -- Paste/Type --> TextSplit[Auto-split to Paragraphs]
    Input -- Upload File --> FileUpload[Upload .txt/.md]
    
    FileUpload --> TextSplit
    
    TextSplit --> Display[Display Paragraphs with Checkboxes]
    Display --> Select[User Clicks to Select/Deselect]
    
    Select --> CheckAuth{Logged In?}
    CheckAuth -- No --> DirectParaphrase[Click 'Paraphrase Selected']
    CheckAuth -- Yes --> SaveOption{Save Draft?}
    
    SaveOption -- Yes --> SaveToDB[Save to D1]
    SaveOption -- No --> DirectParaphrase
    
    DirectParaphrase --> Process[Process Selected Only]
    Process --> Loading[Show Progress & Ads]
    Loading --> API[Call Hono/HF API]
    API --> Result[Display Result]
    
    Result --> Actions{Next Action?}
    Actions -- Copy --> CopyText[Copy to Clipboard]
    Actions -- Download --> Interstitial[Ad Page 5s]
    Actions -- Edit More --> Select
    
    Interstitial --> DownloadFile[Download File]
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
