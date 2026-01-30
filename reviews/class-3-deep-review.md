# Class 3 Deep Pedagogical Review: Geospatial + AI

**Reviewer:** sfc_course_materials/crew/sfcguy
**Date:** 2026-01-30
**Bead:** scm-2fn
**Target Audience:** Non-climate-savvy software engineers, PMs, and designers

---

## Executive Summary

Class 3 introduces the intersection of geospatial data and AI for climate applications, with a focus on satellite imagery, land-use classification, and deforestation detection. The live session slides (3.1) are exceptional - dense with technical content but well-organized with clear frameworks. The async reading is improved over earlier classes with better resource curation. The assignment is practical and achievable. Class 3.2 innovatively uses peer review to reinforce learning.

**Overall Score: 8/10**

The strongest class so far pedagogically. Good scaffolding from concepts to application, excellent real-world examples, and the peer review session in 3.2 is a smart pedagogical choice.

---

## Materials Reviewed

| Material | Source | Status |
|----------|--------|--------|
| Async Reading | class-3.json | Reviewed |
| Slides 3.1 | Google Slides (fetched) | Reviewed |
| Slides 3.2 | Google Slides (fetched) | Reviewed |
| Assignment 3 | Google Doc (fetched) | Reviewed |

---

## Detailed Findings by Material Type

### 1. Async Reading (class-3.json)

**Content Assessment: GOOD**

This async reading is notably better than Classes 1-2:
- Realistic expectations set ("We're not going to master either... we'll aim to get a broad overview")
- Clear learning objectives with practical outcomes
- Curated resources with reading guidance (start with this, then skim/pick)
- Includes a balanced view (AI energy costs article + counterpoint)

**Issues Found:**

#### METADATA MISMATCH (MEDIUM PRIORITY)
- **Location:** class-3.json, `classTitle` field
- **Current:** "Emissions, global warming potentials and the global carbon cycle"
- **Actual Content:** "3. Geospatial + AI"
- **Same issue as Classes 1-2**

#### ACM PAPER MAY REQUIRE AUTHENTICATION (INFO)
- **URL:** https://dl.acm.org/doi/pdf/10.1145/3485128
- **Issue:** Returns 403 Forbidden (paywall/institutional access)
- **Recommendation:**
  - Note that paper may require institutional access
  - Provide alternative: arXiv version may be freely available
  - Or link to summary/overview if exists
- **Note:** Students with university affiliations will likely have access

**Strengths:**
- Excellent resource curation (CTVC methane article, MAAP deforestation, Google methane blog)
- Includes counterpoint to AI energy concerns (balanced view)
- Page-specific reading guidance (ACM paper pg. 2-5, 30-34)
- All resources are from 2022-2024 (current)

### 2. Slides 3.1: Geospatial AI

**Content Assessment: EXCELLENT**

This is the most technically dense class so far, and it handles the complexity well.

**Strengths:**
- Clear "why" section connecting geospatial+AI to climate
- Comprehensive taxonomy of applications (land use, GHG monitoring, weather, renewables siting, etc.)
- Excellent Raster vs. Vector framework with clear definitions
- Electromagnetic spectrum breakdown with practical applications for each band
- Real data source examples (Sentinel-2, MODIS, MethaneSAT)
- Concrete case study (SkyTruth oil spill detection)
- Google Earth Engine primer with data structure concepts
- Interactive poll questions to check understanding

**Issues Found:**

#### OUTDATED SATELLITE STATUS (LOW PRIORITY)
- **Location:** MethaneSAT section
- **Current:** Mentions "lost contact June 2025" and "prototype in orbit as of March 2025"
- **Issue:** Information may be outdated; should verify current MethaneSAT status
- **Recommendation:** Check and update satellite operational status before each cohort

#### DENSE CONTENT WARNING
- **Observation:** This class covers a LOT of ground (raster/vector, EM spectrum, satellite systems, GEE, AI/ML)
- **Not necessarily a problem:** The learning objectives acknowledge this ("broad overview")
- **Recommendation:** Consider adding a summary slide recapping key concepts

**Links Mentioned:**
| Resource | Status | Notes |
|----------|--------|-------|
| Dynamic World (classifier) | Working | Google Earth Engine layer |
| geemap.org | Working | GEE Python library |
| eefabook.org | Working | GEE book resource |
| Cerulean (SkyTruth) | Working | Oil spill detection platform |

### 3. Slides 3.2: Peer Review Session

**Content Assessment: INNOVATIVE**

Class 3.2 departs from lecture format to focus on peer collaboration.

**Strengths:**
- Peer review is an excellent pedagogical technique
- "Strong style" pair programming guidance
- Flexible structure (60 min one notebook or 30/30 alternating)
- Troubleshooting support available (TA Brendan Wells)
- Frames homework as "resume-worthy portfolio project"
- Linked resource for pair programming methodology

**Observations:**
- This format reinforces learning through teaching
- Builds community (course objective #4)
- Helps students who struggled catch up
- Low content density allows for practice

### 4. Assignment 3: Geospatial Land-use Classification Lab

**Content Assessment: STRONG**

**Strengths:**
- Clear learning objectives (4 items)
- Practical Google Earth Engine experience
- Direct application of raster/vector concepts
- Deforestation detection connects to MAAP reading
- Appropriate scope (1-2 hours)
- Encourages original analysis

**Issues Found:**

#### COHORT-SPECIFIC DATE (INFO)
- **Current:** "Friday, October 17, 9:00 AM PT"
- **Note:** Needs updating per cohort

#### HEX NOTEBOOK DEPENDENCY
- **Issue:** Requires "3. Geospatial Land-use Classification" notebook
- **Verification Needed:** Confirm notebook is shared/accessible

---

## Student Perspective Analysis

### Is the jump to geospatial concepts manageable?
**YES, with effort.** The slides provide a solid foundation (raster vs. vector, EM spectrum) before diving into tools. Students may need to revisit the async reading after the live session to fully absorb.

### Is Google Earth Engine well-introduced for newcomers?
**YES.** The slides explain GEE data structures (ImageCollection, FeatureCollection, Reducers) with visual examples. The geemap/eefabook resources provide further learning paths.

### Is the AI/ML component accessible or intimidating?
**ACCESSIBLE.** The slides frame AI as "how we scale insights" rather than requiring deep ML knowledge. The classifier usage is practical (Dynamic World layer) not theoretical (training models from scratch).

### Does the deforestation example resonate?
**YES.** The MAAP Amazon mining case study is compelling and recent (2024 data). Visuals of mining damage in Indigenous territories make the climate connection visceral.

### Is the assignment achievable in the time estimate?
**LIKELY YES.** 1-2 hours is reasonable for exploring GEE and completing structured notebook tasks. Students with prior GIS experience will finish faster.

---

## Pedagogical Expert Perspective

### Is there enough foundation before diving into GEE?
**YES.** Slides 3.1 spends significant time on spatial data concepts before introducing GEE. The raster/vector distinction is clarified first.

### Is the raster vs. vector distinction clear and necessary?
**YES.** This is fundamental to understanding satellite vs. curated data. The framework is introduced early and reinforced with examples throughout.

### Does the content properly connect geospatial→climate solutions?
**EXCELLENT.** Multiple explicit connections:
- Methane monitoring for emissions reduction
- Deforestation detection for forest protection
- Renewables siting for clean energy
- Flood prediction for adaptation

### Is the ML component appropriately scoped?
**YES.** It's practical not theoretical - students use pre-trained classifiers (Dynamic World) rather than building models. This is appropriate for a 1-week module.

### Are the external resources at the right level?
**MIXED:**
- CTVC methane article: Excellent, accessible
- MAAP deforestation: Technical but engaging
- ACM paper: May require institutional access
- AI energy articles: Good balance of perspectives

---

## Link Verification Summary

| Resource | URL | Status | Notes |
|----------|-----|--------|-------|
| ACM ML+Climate paper | dl.acm.org/doi/pdf/10.1145/3485128 | **403 (paywall)** | Requires institutional access |
| CTVC Methane article | ctvc.co/inside-methane-monitorings-big-moment/ | Working | May 2024, current |
| MAAP Deforestation | maaproject.org/maap-212... | Working | 2024, multilingual |
| Google Methane blog | blog.google/outreach-initiatives/sustainability/... | Working | Accessible |
| IEA Electricity PDF | iea.blob.core.windows.net/... | Working | PDF downloadable |
| AI Energy counterpoint | climate.benjames.io/ai-go-brrr/ | Working | Oct 2024-May 2025 |
| geemap.org | geemap.org | Working | GEE Python library |
| eefabook.org | eefabook.org | Working | GEE textbook |

---

## Specific Recommendations

### HIGH PRIORITY

1. **Fix classTitle metadata**
   - **Current:** "Emissions, global warming potentials and the global carbon cycle"
   - **New:** "3. Geospatial + AI"
   - **Location:** class-3.json
   - **Effort:** 2 minutes

2. **Note ACM paper access requirements**
   - Add note that paper may require institutional/library access
   - Consider linking to arXiv preprint if available
   - Or provide executive summary for students without access
   - **Effort:** 15 minutes

### MEDIUM PRIORITY

3. **Verify MethaneSAT operational status**
   - Current slides mention June 2025 contact loss
   - Update with current status before each cohort
   - **Effort:** 10 minutes per cohort

4. **Add summary/recap slide to 3.1**
   - Content is dense; a summary would help retention
   - Key concepts: raster/vector, EM spectrum applications, GEE basics
   - **Effort:** 15 minutes

### LOW PRIORITY

5. **Verify GEE notebook accessibility**
   - Confirm "3. Geospatial Land-use Classification" is shared
   - **Effort:** 5 minutes

6. **Consider adding geemap/Hex compatibility note**
   - Slides mention "geemap's default view has compatibility issues with Hex"
   - Ensure students know how to handle this
   - **Effort:** 5 minutes (already noted in slides)

---

## Cross-Class Alignment Assessment

### Class 2 → Class 3: GOOD
- Class 2 introduced public data sources and APIs
- Class 3 builds on this with satellite data as a specific data source type
- Both use Hex notebooks for hands-on work

### Class 3 → Class 4 (Energy Modeling): ANTICIPATED
- Geospatial skills (siting analysis) will likely connect to energy modeling
- GEE experience provides foundation for spatial energy analysis

### Async → Slides → Assignment: EXCELLENT
- Async introduces ML+climate framework
- Slides expand with technical depth
- Assignment applies specific concepts (GEE, land-use classification)
- Peer review reinforces through teaching

---

## Overall Pedagogical Score: 8/10

**Breakdown:**
- Slides 3.1 content: 9/10 (comprehensive, well-organized, real examples)
- Slides 3.2 format: 9/10 (innovative peer review approach)
- Async reading: 7/10 (good curation, one access-restricted resource)
- Assignment: 8/10 (practical, achievable, connected to concepts)
- Resource quality: 7/10 (mostly excellent, ACM access issue)
- Alignment/sequencing: 9/10 (excellent progression)

**Justification:**
Class 3 is the strongest class reviewed so far. The slides handle complex technical material well, building from foundational concepts (raster/vector, EM spectrum) to practical tools (GEE, Dynamic World). The real-world examples (SkyTruth, MAAP, MethaneSAT) connect abstract concepts to climate impact.

The peer review format in 3.2 is pedagogically smart - it reinforces learning, builds community, and helps struggling students catch up. Framing the homework as "resume-worthy portfolio project" motivates quality work.

The main weakness is the ACM paper access issue, which could frustrate students without institutional access. The metadata mismatch is a recurring pattern that should be fixed across all classes.

For software engineers new to geospatial data, this class provides an excellent introduction that's technical enough to be useful but not so deep as to be overwhelming.

---

## Action Items Summary

| Priority | Item | Status |
|----------|------|--------|
| HIGH | Fix classTitle metadata → "3. Geospatial + AI" | TODO |
| HIGH | Note ACM paper access requirements or provide alternative | TODO |
| MEDIUM | Verify/update MethaneSAT operational status | TODO |
| MEDIUM | Consider adding recap slide to 3.1 | Optional |
| LOW | Verify GEE notebook accessibility | TODO |
| LOW | Confirm geemap/Hex compatibility guidance | Already noted |

---

## Cross-References

- **Related beads:** scm-985 (Course Summation - blocked by this review)
- **Resource index:** async-reading/RESOURCE_INDEX.md
- **Suggested updates:** async-reading/SUGGESTED_UPDATES.md
