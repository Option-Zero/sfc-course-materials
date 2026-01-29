# Review: Classes 1.1 and 1.2 Slides & Async Reading

**Review Date:** 2026-01-28
**Reviewer:** polecat/furiosa
**Issue:** scm-5qq

## Scope

This review covers:
- Async reading: `class-1-1.md` (1.1 Introductions)
- Async reading: `class-1-2.md` (1.2 Software x Climate Landscape)
- Alignment with Google Slides (1.1 Introductions, 1.2 Software x Climate landscape)

**Note:** Google Slides require authentication and could not be directly accessed. Review focuses on async reading content which should mirror slide content.

---

## Class 1.1: Introductions

### Issues Found

#### 1. Typo: "lecutures" → "lectures"
- **Location:** class-1-1.md, line 32
- **Current:** `- **Live sessions** involving lecutures, audience participation`
- **Fix:** `- **Live sessions** involving lectures, audience participation`
- **Severity:** Low (typo)

#### 2. Formatting issue with Slack mention
- **Location:** class-1-1.md, line 35
- **Current:** `Additionally, we have a **cohort slack channel **for ad hoc communication`
- **Fix:** `Additionally, we have a **cohort Slack channel** for ad hoc communication`
- **Severity:** Low (formatting + capitalization)

#### 3. Missing direct links to Python tutorials
- **Location:** class-1-1.md, lines 106-118
- **Issue:** The text mentions "Python cheat sheet & quick reference", "Python tutorial (free)", and "Python tutorial (paid)" but these are not hyperlinked
- **Recommendation:** Add direct URLs:
  - Python cheat sheet: https://www.pythoncheatsheet.org/ or similar
  - Free tutorial: https://docs.python.org/3/tutorial/
  - Codecademy: https://www.codecademy.com/learn/learn-python-3
- **Severity:** Medium (usability)

#### 4. "chomping at the bit" idiom
- **Location:** class-1-1.md, line 125
- **Note:** Traditional phrase is "champing at the bit" but "chomping" is now widely accepted
- **Severity:** None (acceptable variant)

### Links Verified

| Link | Status | Notes |
|------|--------|-------|
| hex.tech/blog/beginners-guide-to-python-notebooks/ | ✅ Working | Content relevant and current |

### Content Review

- **Clarity:** Good overall structure with clear learning objectives
- **Accuracy:** Course format and expectations accurately described
- **Organization:** Well-organized with logical flow from welcome → objectives → reading → conclusion

---

## Class 1.2: Software x Climate Landscape

### Issues Found

#### 1. Broken link: Project Drawdown Foundations
- **Location:** class-1-2.md, line 41
- **Current URL:** https://drawdown.org/drawdown-foundations
- **Issue:** Returns 403 Forbidden
- **Recommendation:**
  - Test manually in browser (may work interactively)
  - Alternative: Link to https://drawdown.org/sectors (which works and includes similar content)
  - Or: Reference Drawdown Explorer which has replaced Foundations content
- **Severity:** Medium (broken link)
- **Note:** Already documented in SUGGESTED_UPDATES.md

#### 2. Dated resource: Bret Victor article (2015)
- **Location:** class-1-2.md, line 51
- **URL:** http://worrydream.com/ClimateChange
- **Issue:** Over 10 years old; climate tech landscape has changed significantly
- **Recommendation:**
  - Keep as foundational reading (still valuable for its framework)
  - Add note about publication date
  - Consider supplementing with recent resources (see SUGGESTED_UPDATES.md)
- **Severity:** Low (content still valuable, just dated)

#### 3. HTTP instead of HTTPS
- **Location:** class-1-2.md, line 51
- **Current:** `http://worrydream.com/ClimateChange`
- **Recommendation:** Update to `https://worrydream.com/ClimateChange` (site supports HTTPS)
- **Severity:** Low (security best practice)

### Links Verified

| Link | Status | Notes |
|------|--------|-------|
| speedandscale.com/tracker/ | ✅ Working | Current data (2024-2025), John Doerr's initiative |
| drawdown.org/drawdown-foundations | ❌ 403 Forbidden | May work in browser; already noted in SUGGESTED_UPDATES.md |
| drawdown.org/sectors | ✅ Working | Drawdown Explorer, comprehensive solutions database |
| climatepapa.com/software | ✅ Working | Ben & Nathan Eidelson's guide |
| climatetechlist.com/blog/bits-vs-atoms-framework | ✅ Working | Steven Zhang, 2023 |
| worrydream.com/ClimateChange | ✅ Working | Bret Victor, 2015 (dated but accessible) |

### Content Review

- **Clarity:** Simple and clear structure
- **Accuracy:** Resources are well-curated for the topic
- **Organization:** Good balance between general frameworks and software-specific resources
- **Currency:** Mix of foundational (2015-2021) and recent (2023) resources

---

## Alignment Check: Async Reading vs. Slides

Based on GDRIVE_STRUCTURE.md, the slides are:
- "1.1 Introductions" (Google Slides)
- "1.2 Software x Climate landscape" (Google Slides)

**Expected alignment:**
- Class 1.1 async reading covers course overview, learning objectives, and Python prep → should align with introductory slides
- Class 1.2 async reading covers software x climate frameworks → should align with landscape overview slides

**Note:** Direct slide content verification requires Google Drive access. Async reading content appears comprehensive and well-structured for the stated learning objectives.

---

## Recommended Updates Summary

### High Priority
1. Fix "lecutures" typo in class-1-1.md
2. Address drawdown.org/drawdown-foundations broken link in class-1-2.md

### Medium Priority
3. Add direct URLs for Python learning resources in class-1-1.md
4. Fix Slack channel formatting in class-1-1.md

### Low Priority
5. Update HTTP to HTTPS for worrydream.com link
6. Consider adding publication dates to resources for transparency

---

## Action Items

- [x] Edit class-1-1.md: Fix "lecutures" typo (line 32) - DONE
- [x] Edit class-1-1.md: Fix Slack formatting (line 35) - DONE
- [x] Edit class-1-1.md: Add Python tutorial URLs (lines 106-118) - DONE
- [x] Edit class-1-2.md: Update drawdown-foundations link to /solutions (line 41) - DONE
- [x] Edit class-1-2.md: Update HTTP to HTTPS for worrydream.com (line 51) - DONE
- [x] Update RESOURCE_INDEX.md: Fix Drawdown URL and worrydream.com HTTPS - DONE
- [x] Update SUGGESTED_UPDATES.md: Mark Drawdown issue as resolved - DONE
