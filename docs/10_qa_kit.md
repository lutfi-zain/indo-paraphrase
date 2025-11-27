# 10. QA Kit 🧪

## 🎯 Test Strategy

### Testing Pyramid
```
        /\
       /  \  E2E Tests (10%)
      /____\
     /      \ Integration Tests (30%)
    /________\
   /          \ Unit Tests (60%)
  /__________/
```

### Test Levels

**1. Unit Tests (Vitest)**
- Individual functions, utilities
- React component rendering
- API route logic (isolated)

**2. Integration Tests**
- API endpoints with D1 mock
- Component + API interaction
- OAuth flow

**3. E2E Tests (Playwright)**
- Full user journeys
- Cross-browser testing
- Mobile viewport

---

## ✅ Test Cases

### TC-001: Basic Paraphrase Flow
**Priority**: P0 (Critical)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open homepage | Textarea visible with placeholder |
| 2 | Paste "Saya suka makan nasi goreng" | Text appears in textarea |
| 3 | Click "Paraphrase" | Loading spinner shows |
| 4 | Wait 2s | Results displayed below |
| 5 | Verify output | Paraphrased text different from original |

**Acceptance Criteria**:
- ✅ Results appear <3 seconds
- ✅ No duplicate paragraphs
- ✅ No error messages

---

### TC-002: Rate Limiting (Free User)
**Priority**: P0 (Critical)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open app (not logged in) | No quota banner |
| 2 | Paraphrase 1st doc | Success, quota banner shows "4/5 remaining" |
| 3 | Paraphrase 5th doc | Success, quota banner shows "0/5 remaining" |
| 4 | Try 6th doc | Error: "Hourly limit reached. Try again in X mins" |
| 5 | Wait 1 hour | Quota resets to 5/5 |

---

### TC-003: Google OAuth Login
**Priority**: P1 (High)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Login" button | Google OAuth popup opens |
| 2 | Select Google account | Popup closes, redirects to app |
| 3 | Check UI | User name + avatar in top-right |
| 4 | Check quota | Banner shows "10/10 docs" (increased) |

---

### TC-004: Save Draft
**Priority**: P1 (High)

**Pre-condition**: User is logged in

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Paste long text (500 words) | Text appears |
| 2 | Click "Paraphrase" | Results show |
| 3 | Click "Save Draft" button | Toast: "Draft saved" |
| 4 | Refresh page | Draft appears in "Your Drafts" sidebar |
| 5 | Click draft | Content loads into editor |

---

### TC-005: Twitter Share Verification
**Priority**: P2 (Medium)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Click "Share to Twitter" | Tweet dialog opens with pre-filled text |
| 2 | Post tweet | Dialog closes |
| 3 | Wait 5s | Backend verifies via API |
| 4 | Check quota | Banner shows "+5 docs bonus added" |

---

### TC-006: Selective Re-paraphrase
**Priority**: P0 (Critical)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Paste 3-paragraph text | Text appears |
| 2 | Click "Paraphrase" | All 3 paragraphs paraphrased |
| 3 | Click paragraph 1 | Paragraph 1 highlighted |
| 4 | Click "Rephrase Selected" (1 para) | Only paragraph 1 re-paraphrased |
| 5 | Verify | Paragraphs 2-3 unchanged |

---

## 🐛 Bug Priority Matrix

| Severity | Critical (P0) | High (P1) | Medium (P2) | Low (P3) |
|----------|---------------|-----------|-------------|----------|
| **Blocker** | App crashes on load | - | - | - |
| **Major** | Paraphrase fails | Login broken | Ad not showing | - |
| **Minor** | - | Typo in UI | Button color off | Privacy link broken |
| **Trivial** | - | - | - | Console warning |

---

## 📊 Quality Checklist

### Before Deploy to Production
- [ ] All P0 test cases pass
- [ ] >80% code coverage
- [ ] No console errors
- [ ] Lighthouse score >90 (Performance, SEO, Accessibility)
- [ ] Cross-browser tested (Chrome, Firefox, Safari)
- [ ] Mobile responsive (375px+)
- [ ] Rate limiting works correctly
- [ ] Ads display properly (non-intrusive)
- [ ] Privacy policy & ToS links work
- [ ] Error pages (`404`, `500`) styled
- [ ] Analytics tracking verified

### Performance Benchmarks
- [ ] TTFB <500ms (global average)
- [ ] FCP <1.5s
- [ ] LCP <2.5s
- [ ] CLS <0.1
- [ ] Paraphrase API response <3s

---

## 🧪 Automated Test Suite

### Run Tests
```bash
# Unit + Integration tests
npm run test

# E2E tests
npm run test:e2e

# Coverage report
npm run test:coverage
```

### CI/CD Integration
Tests run automatically on every PR:
```yaml
name: Tests
on: [pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install
      - run: npm run test
      - run: npm run test:e2e
```

---

## 🔍 Manual QA Smoke Test (5 minutes)

**Before every production deploy**, run this quick checklist:

1. ✅ Homepage loads
2. ✅ Paste text → Paraphrase works
3. ✅ Login with Google works
4. ✅ Save draft works
5. ✅ Load saved draft works
6. ✅ Rate limit shows correctly
7. ✅ Ads visible (not blocking content)
8. ✅ Mobile view looks good
9. ✅ Error handling graceful (paste 10k words)
10. ✅ Download result works

**If ANY fail**: Stop deploy, fix issue, re-test.

---

## 📈 Quality Metrics (Target)

| Metric | Target | Current |
|--------|--------|---------|
| Test Coverage | >80% | TBD |
| Bug Escape Rate | <5% | TBD |
| Mean Time to Detect (MTTD) | <1 hour | TBD |
| Mean Time to Repair (MTTR) | <4 hours | TBD |
| User-Reported Bugs | <10/month | TBD |
