# 8. Agile Backlog 📋

## 🎯 Product Vision

**Vision Statement**: Menjadi platform #1 untuk paraphrase Bahasa Indonesia yang gratis, cepat, dan dipercaya oleh 100k+ mahasiswa dan content writer di Indonesia.

**Success Metrics** (Q1 2025):
- 10k DAU (Daily Active Users)
- 80% user retention (7-day)
- Rp 3jt+ monthly revenue from ads
- <2s average paraphrase time
- 4.5+ rating di Product Hunt

## 📅 Sprint Planning

### Sprint 0: Foundation (Week 1-2) - **DONE** ✅
**Goal**: Setup infrastructure & MVP core

**Completed Stories**:
- ✅ Setup Astro + Hono monorepo
- ✅ Create ParaphraseEditor React component
- ✅ Integrate HuggingFace IndoT5 API
- ✅ Design ad-optimized layout
- ✅ Configure Cloudflare deployment

### Sprint 1: Core Features (Week 3-4) - **IN PROGRESS** 🚧
**Goal**: Complete MVP with rate limiting & auth

| Story ID | User Story | Priority | Story Points | Status |
|----------|-----------|----------|--------------|--------|
| **US-101** | As a user, I want to paste text and see paraphrased results instantly | P0 | 8 | ✅ Done |
| **US-102** | As a user, I want to select specific paragraphs to re-paraphrase | P0 | 5 | 🚧 In Progress |
| **US-103** | As a user, I want fair rate limits (10 para free, 20 para login) | P0 | 8 | ⏳ To Do |
| **US-104** | As a user, I want to login with Google to save drafts | P1 | 13 | ⏳ To Do |
| **US-105** | As a user, I want to see my remaining quota clearly | P1 | 3 | ⏳ To Do |

**Acceptance Criteria** (US-102):
- Given paraphrased results are shown
- When user clicks on a specific paragraph
- Then that paragraph is highlighted as "selected for re-paraphrase"
- And user can click "Rephrase Selected" button
- And only selected paragraphs are sent to API
- And results replace only those paragraphs

**Technical Tasks** (US-103 - Rate Limiting):
- [ ] Create D1 table `rate_limits`
- [ ] Implement IP hashing middleware
- [ ] Implement hourly/daily counter logic
- [ ] Create KV store for fast lookups
- [ ] Add rate limit response headers
- [ ] Show quota banner in UI

### Sprint 2: Monetization & Growth (Week 5-6)
**Goal**: Launch ads & exposure payment

| Story ID | User Story | Priority | Story Points | Assignee |
|----------|-----------|----------|--------------|----------|
| **US-201** | As a user, I want to share to Twitter to get +5 docs bonus | P0 | 8 | Backend |
| **US-202** | As a user, I want a referral link to invite friends | P0 | 5 | Full-stack |
| **US-203** | As an admin, I want to verify Twitter shares automatically | P0 | 13 | Backend |
| **US-204** | As a user, I want to see ads that don't block content | P1 | 5 | Frontend |
| **US-205** | As a user, I want an interstitial ad before download | P2 | 3 | Frontend |

### Sprint 3: Polish & Launch (Week 7-8)
**Goal**: Production-ready, SEO, performance

| Story ID | User Story | Priority | Story Points |
|----------|-----------|----------|--------------|
| **US-301** | As a user, I want fast load times (<2s TTFB) | P0 | 8 |
| **US-302** | As a marketer, I want landing page SEO score 100 | P0 | 5 |
| **US-303** | As a user, I want mobile-responsive design | P0 | 8 |
| **US-304** | As a user, I want to see social proof (user count) | P1 | 3 |
| **US-305** | As a developer, I want error tracking (Sentry) | P1 | 5 |

## 🏗️ Backlog (Prioritized)

### Epic 1: Core Paraphrase Flow
- [x] US-101: Instant paraphrase (paste → results)
- [ ] US-102: Selective re-paraphrase 
- [ ] US-106: File upload (.txt, .md)
- [ ] US-107: Download paraphrased result
- [ ] US-108: Copy to clipboard button
- [ ] US-109: Side-by-side comparison view

### Epic 2: Authentication & User Management
- [ ] US-104: Google OAuth login
- [ ] US-110: Save up to 5 drafts
- [ ] US-111: Auto-save every 30s
- [ ] US-112: Load saved drafts
- [ ] US-113: Delete draft
- [ ] US-114: Account settings page

### Epic 3: Rate Limiting & Fair Usage
- [ ] US-103: Multi-layer rate limiting
- [ ] US-105: Quota display banner
- [ ] US-115: Paragraph word count validator
- [ ] US-116: Auto-chunk long paragraphs
- [ ] US-117: Cooldown timer UI
- [ ] US-118: Fingerprint-based tracking

### Epic 4: Monetization
- [ ] US-204: Ad slots integration (AdSense)
- [ ] US-205: Interstitial ad page
- [ ] US-201: Twitter share verification
- [ ] US-202: Referral program
- [ ] US-119: Weekly contest automation
- [ ] US-120: Premium tier (future)

### Epic 5: SEO & Growth
- [ ] US-302: Landing page SEO optimization
- [ ] US-121: Blog section (/blog)
- [ ] US-122: Open Graph meta tags
- [ ] US-123: Schema.org markup
- [ ] US-124: Sitemap generation
- [ ] US-125: robots.txt

### Epic 6: Quality & Performance
- [ ] US-301: Performance optimization (<2s TTFB)
- [ ] US-303: Mobile responsive design
- [ ] US-126: Accessibility (WCAG 2.1 AA)
- [ ] US-127: Error handling UI
- [ ] US-305: Error tracking (Sentry)
- [ ] US-128: Analytics (Plausible/GA4)

## 🐛 Bug Backlog
| Bug ID | Description | Severity | Reporter | Status |
|--------|-------------|----------|----------|--------|
| BUG-001 | ParaphraseEditor crashes on empty input | High | QA | ✅ Fixed |
| BUG-002 | Layout breaks on mobile <375px width | Medium | User | ⏳ To Do |

## 📊 Definition of Done (DoD)

A user story is "Done" when:
- ✅ Code is written & reviewed (PR approved)
- ✅ Unit tests pass (>80% coverage)
- ✅ Manual QA tested (no critical bugs)
- ✅ Deployed to staging
- ✅ Product Owner approved
- ✅ Deployed to production
- ✅ Monitoring dashboard shows no errors

## 🎲 Story Point Estimation Guide

| Points | Complexity | Time Estimate |
|--------|-----------|---------------|
| 1 | Trivial (CSS change) | <1 hour |
| 3 | Simple (UI component) | 2-4 hours |
| 5 | Medium (API endpoint) | 1 day |
| 8 | Complex (Full feature) | 2-3 days |
| 13 | Very Complex (Multi-service integration) | 1 week |
| 21 | Epic (Break it down!) | - |

## 📈 Velocity Tracking

| Sprint | Planned Points | Completed Points | Velocity |
|--------|---------------|------------------|----------|
| Sprint 0 | 21 | 21 | 100% |
| Sprint 1 | 34 | TBD | - |
| Sprint 2 | 34 | - | - |

**Average Velocity**: 21 points/sprint (2 weeks)

## 🔮 Future Backlog (Post-MVP)

**Q2 2025**:
- Premium tier ($5/month, unlimited docs)
- .docx & .pdf support
- Paraphrase modes (Formal, Casual, Academic)
- Chrome extension
- API for developers ($10/month, 10k requests)

**Q3 2025**:
- Mobile app (React Native)
- Batch processing (upload 10 files at once)
- Custom AI fine-tuning (user-specific style)
- Team collaboration (shared drafts)

**Q4 2025**:
- White-label licensing untuk universities
- Plagiarism checker integration
- Multi-language support (Malay, Tagalog)
