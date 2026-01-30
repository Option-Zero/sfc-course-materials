# Class 2 Deep Pedagogical Review: Public Data Sources

**Reviewer:** sfc_course_materials/crew/sfcguy
**Date:** 2026-01-30
**Bead:** scm-bd5
**Target Audience:** Non-climate-savvy software engineers, PMs, and designers

---

## Executive Summary

Class 2 introduces the concept of public data sources in climate tech, focusing on the "data liquidity play" - using publicly available data to create climate-related value. The live session slides (2.1) are pedagogically strong with excellent structure, real-world case studies, and clear frameworks. However, the async reading content is disappointingly thin, providing little preparation beyond basic resource links. The assignment (Utility Data Lab) is practical and achievable.

**Overall Score: 6.5/10**

The class has solid live session content but suffers from weak async preparation and some broken/outdated links that could frustrate students.

---

## Materials Reviewed

| Material | Source | Status |
|----------|--------|--------|
| Async Reading | class-2.json | Reviewed |
| Slides 2.1 | Google Slides (fetched) | Reviewed |
| Slides 2.2 | Google Slides | Inaccessible (export failed) |
| Assignment 2 | Google Doc (fetched) | Reviewed |

---

## Detailed Findings by Material Type

### 1. Async Reading (class-2.json)

**Content Assessment: WEAK**

The async reading consists of only 4 substantive slides:
1. Title slide
2. Learning objectives (2 items)
3. Resource links (5 data sources to explore)
4. Conclusion ("See you in the live session!")

**Issues Found:**

#### METADATA MISMATCH (MEDIUM PRIORITY)
- **Location:** class-2.json, `classTitle` field
- **Current:** "Emissions, global warming potentials and the global carbon cycle"
- **Actual Content:** "2. Public Data Sources"
- **Impact:** Confusing for any automated processing or indexing; copy-paste error from CL101 course

#### MISSING CONCEPTUAL FOUNDATION
- **Issue:** No explanation of WHY public data matters for climate before asking students to explore resources
- **Impact:** Students may click through resources without understanding the strategic value
- **Recommendation:** Add 2-3 slides explaining the "data liquidity play" concept BEFORE the resources

#### LEARNING OBJECTIVES MISMATCH
- **Stated:** "Understand the value of public data & the 'data liquidity play' in climate tech"
- **Problem:** The async reading never explains what "data liquidity play" means
- **Impact:** Students arrive at live session unprepared for this core concept

### 2. Slides 2.1: Public Data Sources

**Content Assessment: STRONG**

The slides provide excellent pedagogical structure:

**Strengths:**
- Clear agenda with time allocations (90 minutes)
- "Why public data?" section with Newton quote and knowledge visualization
- Practical "Access → Synthesize → Act" framework
- Comprehensive data taxonomy (form, provider, climate alignment)
- Real-world case study (Arcadia) showing the full data→value chain
- Critical design framework warning against data-first thinking
- Brainstorm activity with current resource links (Speed and Scale, IEA)
- Clear "Up Next" section with assignments and bonus events

**Issues Found:**

#### OUTDATED LINK: IEA Tracking Report (LOW PRIORITY)
- **Current:** https://iea.org/reports/tracking-clean-energy-progress-2023
- **Issue:** Links to 2023 report; 2024/2025 versions may be available
- **Recommendation:** Update to latest tracking report or use evergreen URL if available

#### COHORT-SPECIFIC DATE (INFO)
- **Location:** "Up Next" slide
- **Current:** "due Friday, class 2.2"
- **Note:** Dates need updating per cohort

### 3. Assignment 2: Utility Data Lab

**Content Assessment: GOOD**

**Strengths:**
- Clear learning objectives (4 items)
- Reasonable scope (1-2 hours)
- Practical EIA API experience
- Multiple difficulty levels for different coding backgrounds
- Clear deliverables and submission process

**Issues Found:**

#### COHORT-SPECIFIC DUE DATE (INFO)
- **Current:** "Friday, October 10 at 9:00 AM PT"
- **Note:** Needs updating per cohort

#### HEX NOTEBOOK DEPENDENCY
- **Issue:** Assignment requires duplicating "2. Electricity Demand and Generation" notebook
- **Verification Needed:** Confirm this notebook is shared/accessible to students
- **Risk:** If notebook link breaks, entire assignment is blocked

### 4. Resource Links Verification

| Resource | URL | Status | Notes |
|----------|-----|--------|-------|
| EPA eGRID Power Profiler | epa.gov/egrid/power-profiler | Working | Requires JavaScript |
| EIA Grid Monitor | eia.gov/electricity/gridmonitor/... | Timeout issues noted | May need URL update |
| GridStatus.io | gridstatus.io | 403 (bot protection) | Works in browser |
| Climate Tech List | climatetechlist.com/charts | Working | Good jobs data |
| Risk Factor | riskfactor.com | **REDIRECTS** | Now firststreet.org |
| PUDL | catalyst.coop/pudl/ | Working | Excellent resource |
| CTVC | ctvc.co | Working | Good VC data |
| Interconnection.fyi | interconnection.fyi | Working | Current queue data |
| Speed and Scale | speedandscale.com/tracker/ | Working | Updated Sept 2025 |
| Web Scraping Club | substack.thewebscraping.club | Working | Freemium model |

---

## Student Perspective Analysis

### Is the concept of "public data for climate" well motivated?
**PARTIALLY.** The slides motivate it well, but the async reading provides almost no motivation - just "look at these links." Students arrive at the live session having clicked around data portals without understanding the strategic significance.

### Are the data source examples relevant and accessible?
**YES, with caveats.** The resources are genuinely valuable (EPA, EIA, GridStatus, PUDL), but some have accessibility issues (JavaScript requirements, bot protection) that may frustrate exploration.

### Would a software engineer understand why these matter for climate?
**YES - in the live session.** The Arcadia case study brilliantly shows how fragmented utility data becomes a business. The async reading, however, provides no such context.

### Is the assignment achievable?
**YES.** The Utility Data Lab is well-scoped, uses real APIs, and offers appropriate scaffolding through the provided notebook.

### Are there intimidating gaps in assumed knowledge?
**MINOR.** Students need basic Python/pandas familiarity (covered in Class 1). The jump from "here are some data portals" to "now use the EIA API" might feel abrupt for non-technical students.

---

## Pedagogical Expert Perspective

### Does the content build appropriately on Class 1?
**MOSTLY.** Class 1 introduced Python/Hex notebooks; Class 2 applies them to real data. However, the "bits vs atoms" framework from Class 1.2 could be explicitly connected to the data discussion.

### Is the balance of theory vs. hands-on right?
**GOOD in slides, POOR in async.** Slides 2.1 have good conceptual framing before diving into resources. The async reading is all hands-on with no theory.

### Are the external links/resources still valuable and working?
**MOSTLY.** Key issues:
- Risk Factor now redirects to First Street (update needed)
- EIA Grid Monitor has reported timeout issues
- GridStatus.io blocks automated access but works in browsers

### Is anything redundant with what students already know?
**NO.** Class 2 introduces genuinely new material on public data sources.

### Is anything missing that would help connect data→climate impact?
**YES:**
1. No mention of data quality/provenance issues
2. No discussion of how to evaluate whether a data source is trustworthy
3. Missing connection between data access and specific climate outcomes (e.g., "better grid data enables faster renewable integration")

---

## Specific Recommendations

### HIGH PRIORITY

1. **Expand async reading content**
   - Add 2-3 slides explaining "data liquidity play" concept
   - Include a mini case study (can be simplified Arcadia example)
   - Explain the Access → Synthesize → Act framework before resources
   - **Effort:** 1 hour

2. **Fix Risk Factor URL**
   - **Current:** https://riskfactor.com/
   - **New:** https://firststreet.org/
   - **Location:** class-2.json slide 3
   - **Effort:** 5 minutes

3. **Fix classTitle metadata**
   - **Current:** "Emissions, global warming potentials and the global carbon cycle"
   - **New:** "Public Data Sources" or "2. Public Data Sources"
   - **Location:** class-2.json
   - **Effort:** 2 minutes

### MEDIUM PRIORITY

4. **Verify EIA Grid Monitor URL**
   - Test both URLs:
     - https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48
     - https://www.eia.gov/electricity/gridmonitor/dashboard/daily_generation_mix/US48/US48
   - Update to whichever is current/working
   - **Effort:** 10 minutes

5. **Add note about JavaScript/bot protection**
   - Warn students that some resources (EPA Power Profiler, GridStatus.io) may not work well with automated tools but work fine in browsers
   - **Effort:** 5 minutes

6. **Verify Hex notebook accessibility**
   - Confirm "2. Electricity Demand and Generation" notebook is accessible to new cohort members
   - **Effort:** 15 minutes

### LOW PRIORITY

7. **Update IEA link to latest report**
   - Check if 2024 or 2025 version is available
   - **Effort:** 10 minutes

8. **Add connection to Class 1 "bits vs atoms" framework**
   - In async reading, note how data work is "bits" enabling "atoms" (physical infrastructure)
   - **Effort:** 15 minutes

9. **Consider adding data quality discussion**
   - Brief note on how to evaluate data source reliability
   - **Effort:** 30 minutes (if adding content)

---

## Alignment Assessment

### Async Reading ↔ Slides: PARTIAL ALIGNMENT
- Slides cover much more than async reading prepares students for
- Key concept ("data liquidity play") appears in slides but not async reading
- Resource overlap is good, but slides have additional resources

### Slides ↔ Assignment: GOOD ALIGNMENT
- Both focus on EIA data
- Assignment applies concepts taught in slides
- Practical skills match theoretical framework

### Class 2 ↔ Course Arc: GOOD FIT
- Builds naturally on Class 1 Python/notebook intro
- Prepares for Class 3 (Geospatial AI) which will use similar data approaches
- Assignment complexity is appropriate for week 2

---

## Overall Pedagogical Score: 6.5/10

**Breakdown:**
- Slides 2.1 content: 8/10 (excellent structure, real-world examples, clear frameworks)
- Async reading: 4/10 (minimal content, no conceptual foundation)
- Assignment: 7/10 (practical, achievable, appropriate scope)
- Resource quality: 7/10 (valuable resources, some link issues)
- Alignment/sequencing: 7/10 (good fit in course arc, async→live gap)

**Justification:**
The live session content is strong - the Arcadia case study is exactly the kind of real-world example that helps software engineers understand climate data value. However, the async reading is a missed opportunity. Students arrive having clicked around data portals without understanding WHY these matter or the strategic "data liquidity play" concept. This creates unnecessary cognitive load at the start of the live session when students should already have this foundation.

The broken/redirecting links (especially Risk Factor) and metadata errors indicate the materials haven't been recently audited. Quick fixes would raise the score to 7.5/10; expanding the async reading would push it to 8/10.

---

## Action Items Summary

| Priority | Item | Status |
|----------|------|--------|
| HIGH | Expand async reading with conceptual content | TODO |
| HIGH | Fix Risk Factor URL → firststreet.org | TODO |
| HIGH | Fix classTitle metadata | TODO |
| MEDIUM | Verify/update EIA Grid Monitor URL | TODO |
| MEDIUM | Add JavaScript/bot protection note | TODO |
| MEDIUM | Verify Hex notebook accessibility | TODO |
| LOW | Update IEA link to latest report | TODO |
| LOW | Connect to "bits vs atoms" framework | TODO |
| LOW | Add data quality discussion | TODO |
