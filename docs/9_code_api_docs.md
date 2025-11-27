# 9. Code & API Documentation 📖

## 🔌 API Reference

### Base URL
```
Production: https://api.indoparaphrase.com
Development: http://localhost:8787
```

### Authentication
Protected endpoints require JWT token in `Authorization` header:
```
Authorization: Bearer <jwt_token>
```

---

## Endpoints

### `POST /api/paraphrase`
Rephrase paragraphs using IndoT5 model.

**Request:**
```json
{
  "paragraphs": ["string[]"],
  "userId": "string (optional)"
}
```

**Response:**
```json
{
  "results": [
    {
      "original": "string",
      "paraphrased": "string"
    }
  ],
  "quotaRemaining": 18
}
```

**Rate Limits:**
- Free: 5 docs/hour
- Login: 10 docs/hour

---

### `GET /api/rate-limit`
Check current user quota.

**Response:**
```json
{
  "hourly": { "used": 3, "limit": 5, "resetAt": 1701234567 },
  "daily": { "used": 15, "limit": 20, "resetAt": 1701234567 }
}
```

---

### `POST /api/auth/google`
Google OAuth callback endpoint.

**Request:**
```json
{
  "code": "string",
  "redirectUri": "string"
}
```

**Response:**
```json
{
  "token": "jwt_token",
  "user": {
    "id": "string",
    "email": "string",
    "name": "string"
  }
}
```

---

### `POST /api/drafts`
Save document draft (requires auth).

**Request:**
```json
{
  "content": "string",
  "selectedParagraphs": [0, 2, 4]
}
```

**Response:**
```json
{
  "id": 123,
  "message": "Draft saved"
}
```

---

### `GET /api/drafts/:userId`
Load user's saved drafts (requires auth).

**Response:**
```json
{
  "drafts": [
    {
      "id": 123,
      "content": "string",
      "createdAt": 1701234567
    }
  ]
}
```

---

## 🧩 Frontend Components

### `<ParaphraseEditor />`
Main editor component with 3-stage flow.

**Props:**
```typescript
interface ParaphraseEditorProps {
  client?: 'load' | 'idle' | 'visible';
}
```

**Usage:**
```astro
---
import ParaphraseEditor from '../components/ParaphraseEditor';
---

<ParaphraseEditor client:load />
```

**State Management:**
- `input`: User's  text input
- `paragraphs`: Parsed paragraphs with selection state
- `loading`: Paraphrase in progress
- `processed`: Results ready

---

### `<RateLimitBanner />`
Display user's remaining quota.

**Props:**
```typescript
interface RateLimitBannerProps {
  hourlyRemaining: number;
  dailyRemaining: number;
}
```

---

## 📏 Code Standards

### TypeScript
- **Strict mode** enabled
- **No `any`** types (use `unknown` if needed)
- **Explicit return types** for functions
- **Interface** over `type` for objects

### React
- **Function components** only (no class components)
- **Hooks** for state management
- **Props destructuring** in function signature

### File Naming
- Components: `PascalCase.tsx` (e.g., `ParaphraseEditor.tsx`)
- Utils: `camelCase.ts` (e.g., `rateLimiter.ts`)
- API routes: `kebab-case.ts` (e.g., `rate-limit.ts`)

### Testing
- **Unit tests**: Vitest
- **Coverage target**: >80%
- **Test file naming**: `*.test.ts`

**Example:**
```typescript
import { describe, it, expect } from 'vitest';

describe('rateLimiter', () => {
  it('should enforce hourly limit', () => {
    // test
  });
});
```

---

## 🗂️ Project Structure

```
apps/
├── web/                    # Astro frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── layouts/        # Astro layouts
│   │   ├── pages/          # Route pages
│   │   └── styles/         # Global CSS
│   └── public/             # Static assets
└── api/                    # Hono backend
    ├── src/
    │   ├── routes/         # API routes
    │   ├── middleware/     # Auth, CORS, etc
    │   └── utils/          # Helper functions
    └── schema.sql          # D1 schema
```

---

## 🔐 Environment Variables

### Frontend (`apps/web/.env`)
```bash
PUBLIC_API_URL=http://localhost:8787
PUBLIC_GOOGLE_CLIENT_ID=your-client-id
```

### Backend (`apps/api/.env`)
```bash
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-secret
HUGGINGFACE_API_URL=https://hf.space/api/predict
JWT_SECRET=random-secret-key
```
