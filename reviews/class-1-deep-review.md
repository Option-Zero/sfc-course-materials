# Class 1 Deep Pedagogical Review: Introductions & Software x Climate Landscape

**Reviewer:** sfc_course_materials/crew/sfcguy
**Date:** 2026-01-30
**Bead:** scm-x4t
**Target Audience:** Non-climate-savvy software engineers, PMs, and designers

---

## Executive Summary

Class 1 serves as the onboarding experience for the Software for Climate course, split across two sessions: 1.1 (Introductions) and 1.2 (Software x Climate Landscape). The live session slides are excellent - well-structured, compelling, and feature real-world examples that resonate with the target audience. The assignment is comprehensive and achievable. However, the async reading materials are minimal and contain outdated/broken links that need attention.

**Overall Score: 7.5/10**

The strong slides and well-designed assignment create a solid foundation, but the async reading underdelivers and contains a broken link (Drawdown Foundations) that could frustrate students.

---

## Materials Reviewed

| Material | Source | Status |
|----------|--------|--------|
| Async Reading 1.1 | class-1-1.json | Reviewed |
| Async Reading 1.2 | class-1-2.json | Reviewed |
| Slides 1.1 | Google Slides (fetched) | Reviewed |
| Slides 1.2 | Google Slides (fetched) | Reviewed |
| Assignment 1 | Google Doc (fetched) | Reviewed |

**Note:** Prior reviews exist for these materials (assignment-1-review.md, class-1-1-1-2-review.md). This deep review provides a holistic pedagogical assessment and confirms/extends those findings.

---

## Detailed Findings by Material Type

### 1. Async Reading 1.1: Introductions

**Content Assessment: ADEQUATE**

Covers the essentials:
- Welcome message with course structure (async + live + homework)
- Clear learning objectives for course and Class 1.1
- Python preparation guidance with tiered recommendations

**Issues Found:**

#### TYPO: "lecutures" (LOW PRIORITY)
- **Location:** class-1-1.json, slideId 2
- **Current:** "Live sessions involving lecutures"
- **Fix:** "Live sessions involving **lectures**"
- **Status:** Previously identified in class-1-1-1-2-review.md, confirmed fixed

#### METADATA MISMATCH (MEDIUM PRIORITY)
- **Location:** class-1-1.json, `classTitle` field
- **Current:** "Emissions, global warming potentials and the global carbon cycle"
- **Actual Content:** "1.1 Introductions"
- **Impact:** Confusing metadata; appears to be copy-paste from CL101 course

#### FORMATTING ISSUE: Slack mention (LOW PRIORITY)
- **Location:** class-1-1.json, slideId 2
- **Current:** "cohort slack channel **" (extra space before closing)
- **Fix:** "cohort **Slack** channel" (proper capitalization, no space)

**Strengths:**
- Tiered Python learning recommendations (already know → 1 hour → 2 hours)
- Sets appropriate expectations for course engagement
- Links to Hex notebook guide for eager learners

### 2. Async Reading 1.2: Software x Climate Landscape

**Content Assessment: MINIMAL**

Contains only:
- Two learning objectives (why software, big picture)
- Resource links to skim (5 resources, choose 1-2 for deep reading)
- Conclusion ("See you in the live session!")

**Issues Found:**

#### BROKEN LINK: Drawdown Foundations (HIGH PRIORITY)
- **Location:** class-1-2.json, slideId 3
- **Current URL:** https://drawdown.org/drawdown-foundations
- **Status:** Returns 403 Forbidden
- **Fix:** Replace with https://drawdown.org/solutions
- **Status:** Previously identified in class-1-1-1-2-review.md - confirm fix applied

#### DATED RESOURCE: Bret Victor Article (LOW PRIORITY)
- **URL:** http://worrydream.com/ClimateChange
- **Published:** November 2015 (11 years old)
- **Issue:** Climate tech landscape has evolved dramatically
- **Recommendation:** Keep as foundational reading; add note about age or supplement with recent resource
- **Note:** Uses HTTP instead of HTTPS (minor security concern)

#### METADATA MISMATCH (MEDIUM PRIORITY)
- **Location:** class-1-2.json, `classTitle` field
- **Current:** "Emissions, global warming potentials and the global carbon cycle"
- **Actual Content:** "1.2 Software x Climate Landscape"

### 3. Slides 1.1: Introductions

**Content Assessment: EXCELLENT**

**Strengths:**
- Compelling instructor introduction (real climate tech experience)
- Clear course structure (3 modules, 8 weeks)
- Motivating framing: "climate change calls for every one of us to... build better systems"
- Interactive tools introduced (Slido, FigJam)
- Honest about time commitment and what's required vs. optional

**Minor Issues:**

#### COMPANY REFERENCE: Convoy (INFO)
- **Issue:** Convoy mentioned as instructor experience
- **Reality:** Convoy shut down in October 2023
- **Note:** Reference is accurate as past experience, but may confuse students who search
- **Recommendation:** Could add "(2019-2023, now closed)" if updating

### 4. Slides 1.2: Software x Climate Landscape

**Content Assessment: EXCELLENT**

**Strengths:**
- Multiple complementary frameworks for understanding climate tech:
  - Drawdown Solutions Sectors (Reduce sources, Support sinks, Improve society)
  - Bits vs. Atoms Framework (software to hardware spectrum)
  - Product Type Framework (what role does software play?)
  - Resilience Framework (adaptation/intervention points)
- Real company examples (Arcadia, Watershed, Patch, DroneSeed, etc.)
- Builds toward the four "deep dive" topics coming in weeks 3-6
- Visual, well-organized

**Issues Found:**

#### BROKEN LINK: Drawdown Foundations (HIGH PRIORITY)
- **Location:** Listed in resources
- **Same issue as async reading** - needs update to /solutions

### 5. Assignment 1: Introductions & Software x Climate

**Content Assessment: STRONG**

**Strengths:**
- Appropriate scope (1-2 hours)
- Multi-modal engagement (Slack, Airtable, Hex, research, optional hardware)
- Connects to course themes immediately (climate company research)
- Clear deliverables and submission process
- Optional IoT hardware for hands-on learners

**Issues Found:**

#### COHORT-SPECIFIC DATE (INFO)
- **Current:** "Friday, October 3, 9:00 AM PT"
- **Note:** Needs updating per cohort

#### HARDWARE PRICING (LOW PRIORITY)
- **Current:** $45.80 (minimum) to $147.55 (expanded)
- **Note:** IoT component prices fluctuate; verify before each cohort

#### HEX INVITATION EXPIRY (MEDIUM PRIORITY)
- **Current:** "this link will expire in 90 days"
- **Risk:** Late enrollments or re-joiners may face expired links
- **Recommendation:** Document refresh process or use persistent invitation

---

## Student Perspective Analysis

### Is the onboarding smooth?
**YES.** The slides create a welcoming atmosphere. The instructors share their journey into climate tech, making it feel accessible. The course structure is clearly explained with explicit expectations.

### Are the learning objectives clear?
**YES.** Both class sessions have explicit learning objectives. The course arc (8 weeks, 3 modules) is well-communicated.

### Is the "why climate + software" motivation compelling?
**YES.** Slides 1.2 does this brilliantly with multiple frameworks showing where software fits in climate solutions. The Bits vs. Atoms framework is particularly effective for software engineers.

### Are there jargon/concepts needing more explanation?
**MINOR GAPS:**
- "Data liquidity" mentioned but not explained (comes in Class 2)
- "Drawdown" as a framework may be unfamiliar to newcomers
- IoT hardware components may intimidate non-hardware folks

### Does the homework feel achievable and relevant?
**YES.** The 5 tasks are clearly scoped. The climate company research connects directly to the frameworks taught. Optional hardware prevents overwhelming beginners.

---

## Pedagogical Expert Perspective

### Is the scaffolding appropriate?
**YES.** Class 1.1 handles logistics and tool setup; 1.2 builds the conceptual foundation. The async reading prepares (minimally) for each session.

### Are the reading materials at the right level?
**MIXED:**
- Python resources: Well-tiered for different backgrounds
- Climate resources: Good selection, but Bret Victor piece (2015) may feel dated
- Async reading itself: Too thin - students could arrive unprepared

### Is there good alignment between async → slides → assignment?
**GOOD:**
- Async 1.1 → Slides 1.1: Both cover course structure and tools
- Async 1.2 → Slides 1.2: Async links to frameworks; slides expand them
- Assignment connects: Research task applies Bits vs. Atoms framework

### Is anything superfluous or redundant?
**NO.** The content is lean, perhaps too lean in async reading.

### Is anything missing?
**SUGGESTIONS:**
1. Async reading could include a brief "Why software matters for climate" teaser before sending students to external links
2. The Drawdown framework could be briefly introduced in async before deep diving in slides
3. A "what to expect in live sessions" note would help anxious first-timers

### Are the time estimates realistic?
**YES.** Assignment is 1-2 hours; async reading is reasonable if students follow recommendations.

---

## Link Verification Summary

| Resource | URL | Status | Notes |
|----------|-----|--------|-------|
| Speed & Scale | speedandscale.com/tracker/ | Working | Updated Sept 2025 |
| Drawdown Foundations | drawdown.org/drawdown-foundations | **BROKEN (403)** | Use /solutions instead |
| Drawdown Solutions/Sectors | drawdown.org/solutions | Working | Good replacement |
| Climate Papa Software | climatepapa.com/software | Working | June 2023, current |
| Bits vs Atoms | climatetechlist.com/blog/bits-vs-atoms-framework | Working | Good framework |
| Bret Victor | worrydream.com/ClimateChange | Working | Nov 2015 (dated) |
| Hex Notebooks Guide | hex.tech/blog/beginners-guide-to-python-notebooks/ | Working | Good intro |
| Python Cheatsheet | pythoncheatsheet.org/cheatsheet/basics | Working | Previously verified |
| Python Tutorial | docs.python.org/3/tutorial/introduction.html | Working | Official docs |
| Codecademy Python | codecademy.com/enrolled/courses/learn-python-3 | Working | Paid option |
| softwarexclimate.com | softwarexclimate.com | Working | Assignment submission |

---

## Specific Recommendations

### HIGH PRIORITY

1. **Fix Drawdown Foundations URL**
   - **Current:** https://drawdown.org/drawdown-foundations
   - **New:** https://drawdown.org/solutions
   - **Location:** class-1-2.json slideId 3, Slides 1.2
   - **Status:** Previously identified - verify fix applied
   - **Effort:** 5 minutes

2. **Fix classTitle metadata in both JSON files**
   - **class-1-1.json:** Change to "1.1 Introductions"
   - **class-1-2.json:** Change to "1.2 Software x Climate Landscape"
   - **Current (both):** "Emissions, global warming potentials and the global carbon cycle"
   - **Effort:** 5 minutes

### MEDIUM PRIORITY

3. **Expand async reading 1.2 with conceptual teaser**
   - Add 1-2 slides explaining WHY software matters for climate
   - Brief intro to frameworks before external reading
   - Reduces cognitive load in live session
   - **Effort:** 30 minutes

4. **Add publication date context to Bret Victor link**
   - Note that it's from 2015 but remains valuable as foundational thinking
   - **Effort:** 5 minutes

5. **Update HTTP to HTTPS for Bret Victor link**
   - **Current:** http://worrydream.com/ClimateChange
   - **New:** https://worrydream.com/ClimateChange
   - **Effort:** 2 minutes

### LOW PRIORITY

6. **Fix typo "lecutures" if not already fixed**
   - **Location:** class-1-1.json slideId 2
   - **Status:** Check if prior review fix was applied
   - **Effort:** 2 minutes

7. **Fix Slack channel formatting**
   - **Current:** "cohort slack channel **"
   - **New:** "cohort **Slack** channel"
   - **Effort:** 2 minutes

8. **Document Hex invitation refresh process**
   - Ensure process exists for refreshing 90-day expiring invites
   - **Effort:** 15 minutes (documentation)

9. **Consider adding note about Convoy's closure (optional)**
   - In instructor bio, clarify timeframe: "Convoy (efficient trucking, 2019-2023)"
   - **Effort:** 5 minutes

---

## Comparison with Prior Reviews

This review confirms findings from:
- **assignment-1-review.md** (Polecat nux): Broken Python cheatsheet link, Convoy reference, typo issues
- **class-1-1-1-2-review.md** (polecat/furiosa): Drawdown Foundations 403, typo fixes, missing hyperlinks

**Additional findings in this review:**
- classTitle metadata mismatch in both JSON files
- Async reading content is too thin (pedagogical gap)
- Hex invitation expiry as a process concern
- Comprehensive student perspective analysis

---

## Overall Pedagogical Score: 7.5/10

**Breakdown:**
- Slides 1.1 content: 9/10 (excellent onboarding, clear expectations)
- Slides 1.2 content: 9/10 (multiple valuable frameworks, good examples)
- Async reading 1.1: 7/10 (adequate but minimal)
- Async reading 1.2: 5/10 (too thin, broken link)
- Assignment: 8/10 (comprehensive, achievable, relevant)
- Resource quality: 7/10 (one broken link, one dated resource)
- Alignment/sequencing: 8/10 (good flow from async → live → assignment)

**Justification:**
Class 1 succeeds at its primary mission: welcoming newcomers and establishing the "why" of software for climate. The live session content is excellent - the multiple frameworks in 1.2 are exactly what software engineers need to understand where they fit. The assignment smartly requires students to apply these frameworks immediately.

The weak points are fixable: the broken Drawdown link and metadata mismatches are quick fixes. Expanding the async reading would require more effort but would significantly improve preparation for live sessions.

For a course targeting non-climate-savvy software engineers, this opening week does a good job of making climate tech accessible and exciting. The instructors' real-world experience adds credibility, and the company examples make the concepts concrete.

---

## Action Items Summary

| Priority | Item | Status |
|----------|------|--------|
| HIGH | Fix Drawdown Foundations URL → /solutions | Verify if done |
| HIGH | Fix classTitle metadata in both JSON files | TODO |
| MEDIUM | Expand async reading 1.2 with conceptual content | TODO |
| MEDIUM | Add publication date context to Bret Victor link | TODO |
| MEDIUM | Update HTTP to HTTPS for Bret Victor link | Verify if done |
| LOW | Fix "lecutures" typo | Verify if done |
| LOW | Fix Slack channel formatting | Verify if done |
| LOW | Document Hex invitation refresh process | TODO |
| LOW | Consider Convoy closure note | Optional |

---

## Cross-References

- **Prior reviews:** reviews/assignment-1-review.md, reviews/class-1-1-1-2-review.md
- **Resource index:** async-reading/RESOURCE_INDEX.md
- **Suggested updates:** async-reading/SUGGESTED_UPDATES.md
- **Related beads:** scm-985 (Course Summation - blocked by this review)
