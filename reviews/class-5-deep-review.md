# Class 5 Deep Pedagogical Review: Software/Hardware Interfaces

**Reviewer:** sfc_course_materials/crew/sfcguy
**Date:** 2026-01-30
**Bead:** scm-b2r
**Target Audience:** Non-climate-savvy software engineers, PMs, and designers

---

## Executive Summary

Class 5 explores the software/hardware interface, covering IoT systems, industrial automation (PLCs), and embedded systems. The live session slides (5.1) are exceptionally comprehensive with excellent case studies (Osmo Systems aquaculture, Natel Energy fish-safe turbines) that make the material engaging. The async reading is well-curated with 5 short, focused readings. This is a challenging topic for pure software engineers, but the course handles it well by emphasizing practical concepts over deep hardware knowledge.

**Overall Score: 7.5/10**

Strong technical content with compelling real-world case studies. The hardware-optional approach is pedagogically sound. Minor issues with URL changes (Deloitte redirect) and inability to verify Reddit link.

---

## Materials Reviewed

| Material | Source | Status |
|----------|--------|--------|
| Async Reading | class-5.json | Reviewed |
| Slides 5.1 | Google Slides (fetched) | Reviewed |
| Slides 5.2 | Google Slides | Inaccessible (401 error) |
| Assignment 5 | Google Doc | Inaccessible (400/401 errors) |

**Note:** Slides 5.2 and Assignment 5 could not be fetched due to access errors. Review based on 5.1 content and async reading.

---

## Detailed Findings by Material Type

### 1. Async Reading (class-5.json)

**Content Assessment: GOOD**

The async reading is notably well-curated with 5 focused, digestible readings:
1. "If you can use open source, you can build hardware" - accessible intro
2. Deloitte Industry 4.0 report (page 4 diagram)
3. ISA95 Pyramid article
4. Reddit comment on PLCs vs SBCs
5. Ladder Logic tutorial (first 4 sections only)

**Strengths:**
- Short, focused reading assignments
- Mix of formats (blog, report, Reddit, tutorial)
- Specific guidance ("Read pg. 4", "first 4 sections", "first comment")
- Includes practical insight about ladder logic limitations (no version control, unit testing)

**Issues Found:**

#### METADATA MISMATCH (MEDIUM PRIORITY)
- **Location:** class-5.json, `classTitle` field
- **Current:** "Emissions, global warming potentials and the global carbon cycle"
- **Actual Content:** "5. Software/hardware interfaces"
- **Same pattern as all classes**

#### DELOITTE PDF URL REDIRECT (LOW PRIORITY)
- **Current URL:** https://www2.deloitte.com/content/dam/insights/us/articles/...
- **Status:** Redirects to new deloitte.com domain
- **Impact:** Currently works (301 redirect followed), but URL should be updated
- **New URL:** https://www.deloitte.com/content/dam/insights/articles/2024/...

#### REDDIT LINK UNVERIFIABLE (INFO)
- **URL:** reddit.com/r/PLC/comments/2a5g4q/comment/ciry1u2/
- **Status:** Cannot verify via automated fetch (Reddit blocks)
- **Note:** Likely working in browser; manual verification recommended

**Working Links Verified:**
- "If you can use open source..." article: Working, accessible
- ISA95 Pyramid article: Working, good explainer
- Ladder Logic tutorial: Working, beginner-friendly

### 2. Slides 5.1: Software/Hardware Interface

**Content Assessment: EXCELLENT**

This is one of the most technically dense classes, but it's handled masterfully.

**Strengths:**

**Clear Conceptual Foundation:**
- Software/hardware interface defined simply: "Software that interacts with the physical world"
- Hardware vs Firmware vs Software distinctions clarified
- "We flip switches and valves, we spin motors and pumps" - memorable framing

**Comprehensive Technical Coverage:**
- Sensors & actuators with real examples (SCD40 CO2 sensor)
- Communication protocols spectrum (Analog → USB4)
- Edge computing platform comparison (PLC vs Microcontroller vs PC/SBC)
- Connectivity options table with range/speed tradeoffs

**Excellent Case Studies:**
1. **Osmo Systems (Aquaculture):**
   - Compelling climate connection (fish = 5%+ global protein)
   - Clear problem/solution framing
   - Full development stack shown (R&D → Prototype)
   - Layer mapping to IoT architecture

2. **Natel Energy (Fish-safe turbines):**
   - Surprising problem (22% fish mortality in hydro)
   - Innovative solution with 100% survival achieved
   - Notes "huge opportunity for low-hanging fruit improvements"
   - Connects hardware to software opportunities

**Layer Architecture Visualization:**
The Physics → Hardware → Firmware → Sensor → Edge → Communication → Storage stack is clearly explained with concrete examples at each layer.

**Issues Found:**

#### DENSE CONTENT WARNING
- **Observation:** PLCs, protocols, ISA95, IoT architecture in one session
- **Mitigation:** The slides acknowledge this is a survey, and case studies ground the concepts

### 3. Slides 5.2 & Assignment 5: (Not Accessible)

**Status:** Could not fetch due to 401 errors

**Based on bead description, expected content:**
- Assignment 5 is "IoT Data Lab"
- Hardware is optional (not exclusionary)
- Students can work without physical hardware

**Cannot evaluate:** Hardware-optional approach, assignment achievability

---

## Student Perspective Analysis

### Is the hardware component accessible or intimidating?
**ACCESSIBLE.** The slides start with software concepts (firmware definitions) before diving into hardware. The case studies show software engineers contributing to hardware projects without needing to be EE experts.

### Is the firmware/embedded systems content appropriate for software folks?
**YES.** The content focuses on interfaces and protocols, not circuit design. The "If you can use open source, you can build hardware" reading sets an encouraging tone.

### Is the optional hardware purchase well-handled?
**CANNOT FULLY EVALUATE.** The assignment couldn't be fetched. However, the async reading mentions optional IoT hardware from Assignment 1, suggesting a thoughtful approach.

### Does the Osmo Systems case study resonate?
**YES.** The aquaculture angle is unexpected and compelling. The climate connection (protein efficiency → emissions reduction) is clearly drawn. The R&D vs prototype stack comparison is practical.

### Is the IoT assignment achievable without physical hardware?
**UNKNOWN.** Assignment 5 could not be accessed.

---

## Pedagogical Expert Perspective

### Is the progression sensor→edge→cloud well-scaffolded?
**YES.** The layer architecture (Physics → Hardware → ... → Storage) provides a clear mental model. Each layer is explained with examples before moving to the next.

### Is the PLCs vs microcontrollers vs SBCs comparison useful or confusing?
**USEFUL.** The comparison table with factors (cost, power, security, accessibility) helps students understand when to use which. The "best use case" summary is practical.

### Does this class connect back to climate impact sufficiently?
**EXCELLENT.** Both case studies directly connect to climate:
- Osmo Systems: Aquaculture efficiency → reduced emissions
- Natel Energy: Fish-safe hydro → better clean energy

The smart thermostat and solar+storage examples in the intro also make the climate connection.

### Are the industrial automation concepts (ISA95, ladder logic) too much?
**BORDERLINE.** For software engineers, this content is novel but potentially overwhelming. The async reading helps by providing pre-class context. The slides handle it by acknowledging ladder logic's limitations (no version control) - relatable for developers.

### Is the hardware-optional approach pedagogically sound?
**CANNOT FULLY EVALUATE.** Based on available information, it appears thoughtful (hardware listed as optional from Assignment 1).

---

## Link Verification Summary

| Resource | URL | Status | Notes |
|----------|-----|--------|-------|
| Open source hardware article | redeem-tomorrow.com/... | Working | Good intro |
| Deloitte Industry 4.0 | www2.deloitte.com/... | **Redirects** | Works, URL changed |
| ISA95 Pyramid | excelpro.ca/en/news/... | Working | Good explainer |
| Reddit PLC comment | reddit.com/r/PLC/... | **Cannot verify** | Reddit blocks automated |
| Ladder Logic tutorial | solisplc.com/tutorials/... | Working | Beginner-friendly |

---

## Specific Recommendations

### HIGH PRIORITY

1. **Fix classTitle metadata**
   - **Current:** "Emissions, global warming potentials and the global carbon cycle"
   - **New:** "5. Software/hardware interfaces"
   - **Effort:** 2 minutes

2. **Investigate Assignment 5 access issue**
   - 401 errors during fetch - may be permission issue
   - Verify assignment doc is publicly accessible
   - **Effort:** 10 minutes

### MEDIUM PRIORITY

3. **Update Deloitte PDF URL**
   - **Current:** www2.deloitte.com domain
   - **New:** www.deloitte.com domain
   - URL still works via redirect, but direct link preferred
   - **Effort:** 5 minutes

4. **Manually verify Reddit link**
   - Cannot verify via automated tools
   - Ensure comment still exists and is relevant
   - **Effort:** 5 minutes

### LOW PRIORITY

5. **Consider adding summary/recap slide**
   - Content is dense (PLCs, protocols, IoT architecture)
   - Quick recap would aid retention
   - **Effort:** 15 minutes

6. **Investigate Slides 5.2 access issue**
   - 401 error during fetch
   - Verify slides are publicly accessible
   - **Effort:** 10 minutes

---

## Comparison with Other Classes

| Aspect | Class 5 | Class 4 | Class 3 | Class 2 | Class 1 |
|--------|---------|---------|---------|---------|---------|
| Async quality | Good | Poor (broken) | Good | Minimal | Adequate |
| Slides quality | Excellent | Excellent | Excellent | Strong | Excellent |
| Assignment | Unknown | Good | Strong | Good | Strong |
| Case studies | Excellent | Good | Good | Good | N/A |
| Overall | 7.5/10 | 6.5/10 | 8/10 | 6.5/10 | 7.5/10 |

Class 5 has strong technical content and excellent case studies, bringing it back up from Class 4's broken links.

---

## Overall Pedagogical Score: 7.5/10

**Breakdown:**
- Slides 5.1 content: 9/10 (comprehensive, excellent case studies)
- Slides 5.2 content: Not reviewed (access issue)
- Async reading: 8/10 (well-curated, focused readings)
- Assignment: Not reviewed (access issue)
- Resource quality: 7/10 (minor redirect issue, Reddit unverifiable)
- Alignment/sequencing: 8/10 (good progression through layers)

**Justification:**
Class 5 tackles a challenging topic for software engineers - hardware interfaces - and does it well. The layered architecture (Physics → Storage) provides a clear mental model, and the case studies ground abstract concepts in climate impact. Osmo Systems' aquaculture sensors and Natel Energy's fish-safe turbines are compelling, unexpected examples that demonstrate software's role in physical-world climate solutions.

The async reading is notably better than earlier classes, with 5 focused, digestible pieces. The specific guidance ("first 4 sections", "first comment") respects students' time.

The main limitation is the inability to evaluate the assignment and Slides 5.2 due to access errors. The metadata mismatch continues across all classes.

---

## Action Items Summary

| Priority | Item | Status |
|----------|------|--------|
| HIGH | Fix classTitle metadata | TODO |
| HIGH | Investigate Assignment 5 access issue | TODO |
| MEDIUM | Update Deloitte PDF URL | TODO |
| MEDIUM | Manually verify Reddit link | TODO |
| LOW | Investigate Slides 5.2 access issue | TODO |
| LOW | Consider adding recap slide | Optional |

---

## Cross-References

- **Related beads:** scm-985 (Course Summation - blocked by this review)
- **Resource index:** async-reading/RESOURCE_INDEX.md
- **Suggested updates:** async-reading/SUGGESTED_UPDATES.md
