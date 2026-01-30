# Class 4 Deep Pedagogical Review: Energy Modeling

**Reviewer:** sfc_course_materials/crew/sfcguy
**Date:** 2026-01-30
**Bead:** scm-zhn
**Target Audience:** Non-climate-savvy software engineers, PMs, and designers

---

## Executive Summary

Class 4 covers energy modeling in climate tech, focusing on building energy usage, renewable generation, energy storage, and grid transmission. The live session slides (4.1) are comprehensive and well-organized, with an excellent case study (Energy Raven) that shows practical application. However, the async reading has TWO broken links (JP Morgan PDF and AIA guide), which is a significant issue. The two-option assignment format is innovative but may cause decision paralysis.

**Overall Score: 6.5/10**

Strong conceptual content undermined by broken links in async reading. The Energy Raven case study is excellent, but students may arrive unprepared if they can't access the recommended readings.

---

## Materials Reviewed

| Material | Source | Status |
|----------|--------|--------|
| Async Reading | class-4.json | Reviewed |
| Slides 4.1 | Google Slides (fetched) | Reviewed |
| Slides 4.2 | Google Slides | Inaccessible (401 error) |
| Assignment 4 | Google Doc (fetched) | Reviewed |

**Note:** Slides 4.2 returned 401 Unauthorized error during fetch. Review based on 4.1 content only.

---

## Detailed Findings by Material Type

### 1. Async Reading (class-4.json)

**Content Assessment: PROBLEMATIC**

The async reading has good pedagogical structure but is severely undermined by broken links.

**Issues Found:**

#### BROKEN LINK: JP Morgan "Growing Pains" PDF (HIGH PRIORITY)
- **URL:** https://assets.jpmprivatebank.com/content/dam/jpm-wm-aem/campaign/energy-paper-13/growing-pains-renewable-transition-in-adolescence.pdf
- **Status:** Returns 404 Not Found
- **Impact:** This is the PRIMARY recommended reading (pages 5-6, 15, 35)
- **Previously noted:** In SUGGESTED_UPDATES.md with replacement URL
- **Replacement:** https://am.jpmorgan.com/content/dam/jpm-am-aem/global/campaign/energy-paper-13/growing-pains-renewable-transition-in-adolescence.pdf

#### BROKEN LINK: AIA Energy Modeling Guide (HIGH PRIORITY)
- **URL:** https://content.aia.org/sites/default/files/2016-04/Energy-Modeling-Design-Process-Guide.pdf
- **Status:** Redirects to AIA homepage (301), PDF not accessible
- **Impact:** Recommended reading (pages 10-14)
- **Note:** This guide is from 2016 (10 years old); may need modern replacement

#### METADATA MISMATCH (MEDIUM PRIORITY)
- **Location:** class-4.json, `classTitle` field
- **Current:** "Emissions, global warming potentials and the global carbon cycle"
- **Actual Content:** "4. Energy modeling"
- **Same pattern as all other classes**

**Working Links:**
- Volts podcast on interconnection queues: Working, accessible (audio + transcript)

**Strengths (when links work):**
- Clear framing: "Electrify everything" + "Decarbonize the grid"
- Page-specific reading guidance
- Prioritized reading order
- Includes podcast option for audio learners

### 2. Slides 4.1: Energy Modeling

**Content Assessment: EXCELLENT**

Despite async reading issues, the slides are comprehensive and well-structured.

**Strengths:**
- Clear "Why Energy Modeling?" framing with two-part decarbonization strategy
- Four categories of energy modeling clearly delineated:
  1. Building Energy Usage Modeling
  2. Renewable Generation Modeling
  3. Energy Storage Systems Modeling
  4. Transmission & Grid Modeling
- Each category includes: Why model? Key aspects, Tools, Resources
- Excellent tool coverage (OpenStudio, EnergyPlus, pvlib, GenX, PyBaMM)
- Storage duration types explained (SD, LDS, MDS) with rationale
- Practical case study (Energy Raven) showing real implementation

**Energy Raven Case Study - HIGHLIGHTS:**
- Clear problem statement (homeowner activation energy)
- Insight about home buying as catalyst moment
- Technical architecture shown (EnergyPlus/OpenStudio in Docker on AWS ECS)
- Data sources explained (satellite imagery, NREL ResStock, utility data, tax assessor)
- End-to-end workflow from inspector data to homebuyer report

**Issues Found:**

#### DENSE CONTENT
- **Observation:** Four full modeling categories in one 90-minute session
- **Risk:** Students may feel overwhelmed
- **Mitigation:** The slides acknowledge this is a survey, not deep dive

### 3. Slides 4.2: (Not Accessible)

**Status:** Could not fetch due to 401 Unauthorized error

**Note:** Unable to review 4.2 content. Based on Class 3 pattern, this may be a peer review session.

### 4. Assignment 4: Energy Modeling Lab

**Content Assessment: INNOVATIVE BUT POTENTIALLY CONFUSING**

**Strengths:**
- Choice between two options respects different interests
- Both options are practical and produce tangible results
- Extra credit for completing both encourages deeper engagement
- Appropriate time estimate (1-2 hours)

**Option A: Solar PV Modeling**
- Model residential rooftop solar
- Uses weather data and PV characteristics
- Outputs electricity generation simulation

**Option B: HVAC Modeling**
- Model home heating/cooling system
- Uses building envelope and weather data
- Outputs electricity usage simulation

**Issues Found:**

#### DECISION PARALYSIS RISK (MEDIUM PRIORITY)
- **Issue:** Students must choose without clear guidance on which is "better"
- **Impact:** Some students may waste time deciding
- **Recommendation:** Add brief guidance: "Choose A if interested in generation, B if interested in efficiency" or "Choose based on your final project direction"

#### COHORT-SPECIFIC DATE (INFO)
- **Current:** "Friday, October 24 at 9:00 AM PT"
- **Note:** Needs updating per cohort

---

## Student Perspective Analysis

### Is "energy modeling" well-defined for someone unfamiliar?
**YES.** The slides clearly define it as modeling electricity usage, generation, storage, and transmission. The four-category taxonomy provides a mental map.

### Is the electrification narrative clear and compelling?
**YES.** "Electrify everything + Decarbonize the grid" is a simple, memorable framing. The 21% current renewable status provides concrete context.

### Are the tools (pvlib, EnergyPlus) introduced at the right level?
**YES.** Tools are mentioned with purpose (what they do, why use them) without requiring prior knowledge. Links provided for deeper exploration.

### Is choosing between Option A and B clear? Are both equally valuable?
**PARTIALLY.** Both are valuable, but students may struggle to choose without guidance on which fits their interests or final project direction.

### Is the Energy Raven case study relatable?
**YES.** Home energy is universally relatable. The insight about home buying as a "moment of openness" is clever and memorable.

---

## Pedagogical Expert Perspective

### Is the scope appropriate?
**BORDERLINE.** Four full modeling categories is ambitious for one session. The survey approach works, but depth is sacrificed.

### Is the building energy vs grid energy distinction clear?
**YES.** The four categories separate building (Category 1) from grid-level concerns (Categories 2-4) clearly.

### Does the content connect to real climate impact?
**YES.** The electrification narrative directly connects to emissions reduction. Storage explanation addresses renewable intermittency.

### Are the physics concepts accessible without being oversimplified?
**YES.** Thermal energy flows (conduction, solar radiation, air leaks) are explained without equations. Storage duration types are practical, not theoretical.

### Is the two-option assignment good pedagogy or confusing?
**MIXED.** Good: respects student autonomy and interests. Potentially confusing: no clear decision criteria provided.

---

## Link Verification Summary

| Resource | URL | Status | Notes |
|----------|-----|--------|-------|
| JP Morgan "Growing Pains" | assets.jpmprivatebank.com/... | **404 NOT FOUND** | URL changed |
| Volts Podcast | volts.wtf/p/whats-the-deal-with-interconnection | Working | Audio + transcript |
| AIA Energy Modeling Guide | content.aia.org/sites/default/files/2016-04/... | **REDIRECTS (broken)** | Moved to new AIA site |
| OpenStudio | openstudio.net | Working | NREL tool |
| pvlib-python | pvlib-python.readthedocs.io | Working | Python library |
| GenX | energy.mit.edu/genx | Working | MIT tool |
| Form Energy | formenergy.com | Working | Storage planning |
| PyBaMM | pybamm.org | Working | Battery modeling |
| Interconnection.fyi | interconnection.fyi | Working | Queue tracking |

---

## Specific Recommendations

### HIGH PRIORITY

1. **Fix JP Morgan PDF URL**
   - **Current:** https://assets.jpmprivatebank.com/content/dam/jpm-wm-aem/campaign/energy-paper-13/growing-pains-renewable-transition-in-adolescence.pdf
   - **New:** https://am.jpmorgan.com/content/dam/jpm-am-aem/global/campaign/energy-paper-13/growing-pains-renewable-transition-in-adolescence.pdf
   - **Alternative:** https://privatebank.jpmorgan.com/content/dam/jpm-wm-aem/global/cwm/en/insights/eye-on-the-market/2023-annual-energy-paper-jpmwm.pdf
   - **Location:** class-4.json slideId 3
   - **Effort:** 5 minutes

2. **Fix or replace AIA Energy Modeling Guide**
   - **Current:** content.aia.org link is broken
   - **Options:**
     - Find current location on AIA website
     - Replace with more recent resource (guide is from 2016)
     - Consider: ClimateStudio documentation or ASHRAE resources
   - **Location:** class-4.json slideId 3
   - **Effort:** 30 minutes (to find suitable replacement)

3. **Fix classTitle metadata**
   - **Current:** "Emissions, global warming potentials and the global carbon cycle"
   - **New:** "4. Energy Modeling"
   - **Effort:** 2 minutes

### MEDIUM PRIORITY

4. **Add decision guidance for Assignment 4 options**
   - Help students choose between Option A (solar) and Option B (HVAC)
   - Suggested guidance: "Choose A if interested in renewable generation, B if interested in building efficiency"
   - **Effort:** 10 minutes

5. **Investigate Slides 4.2 access issue**
   - 401 error during fetch - may be permission issue
   - Verify slides are publicly accessible
   - **Effort:** 10 minutes

### LOW PRIORITY

6. **Consider adding summary/recap slide**
   - Four modeling categories is dense
   - Quick recap would aid retention
   - **Effort:** 15 minutes

---

## Comparison with Other Classes

| Aspect | Class 4 | Class 3 | Class 2 | Class 1 |
|--------|---------|---------|---------|---------|
| Async quality | Poor (2 broken links) | Good | Minimal | Adequate |
| Slides quality | Excellent | Excellent | Strong | Excellent |
| Assignment | Good (innovative) | Strong | Good | Strong |
| Overall | 6.5/10 | 8/10 | 6.5/10 | 7.5/10 |

Class 4 has excellent conceptual content but is let down by broken links that will frustrate students.

---

## Overall Pedagogical Score: 6.5/10

**Breakdown:**
- Slides 4.1 content: 9/10 (comprehensive, well-organized, excellent case study)
- Slides 4.2 content: Not reviewed (access issue)
- Async reading: 4/10 (good structure but 2 broken links)
- Assignment: 7/10 (innovative but needs decision guidance)
- Resource quality: 5/10 (2 of 3 main resources broken)
- Alignment/sequencing: 7/10 (good progression from concepts to tools)

**Justification:**
The slides for Class 4 are among the best in the course - the four-category taxonomy is clear, the tools coverage is practical, and the Energy Raven case study is exactly what software engineers need to see (real architecture, real data sources, real workflow). However, the two broken links in async reading are a critical failure. Students who follow the instructions ("Read pages 5-6 in Growing Pains") will hit a 404 error, which is frustrating and undermines trust in the materials.

The two-option assignment is pedagogically interesting but risks decision paralysis. Adding brief guidance on how to choose would significantly improve the student experience.

Fixing the broken links would immediately raise the score to 7.5-8/10.

---

## Action Items Summary

| Priority | Item | Status |
|----------|------|--------|
| HIGH | Fix JP Morgan PDF URL (404) | TODO |
| HIGH | Fix/replace AIA Energy Modeling Guide (broken) | TODO |
| HIGH | Fix classTitle metadata | TODO |
| MEDIUM | Add decision guidance for A/B assignment options | TODO |
| MEDIUM | Investigate Slides 4.2 access issue | TODO |
| LOW | Consider adding summary/recap slide | Optional |

---

## Cross-References

- **Broken links also noted in:** async-reading/SUGGESTED_UPDATES.md
- **Related beads:** scm-985 (Course Summation - blocked by this review)
- **Resource index:** async-reading/RESOURCE_INDEX.md
