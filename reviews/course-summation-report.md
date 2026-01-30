# Course Summation Report: Software for Climate

**Reviewer:** sfc_course_materials/crew/sfcguy
**Date:** 2026-01-30
**Bead:** scm-985

---

## 1. Executive Summary

### Overall Course Quality Assessment

The Software for Climate course is a **well-designed, practical introduction** to climate tech for software engineers. The live session content is consistently excellent, featuring clear frameworks, real-world case studies, and hands-on assignments. However, the course is undermined by **infrastructure issues** (broken links, thin async reading, access errors) that create friction for students.

**Composite Score: 7.2/10**

| Class | Score | Highlight |
|-------|-------|-----------|
| Class 1: Introductions | 7.5/10 | Strong frameworks (Bits vs Atoms) |
| Class 2: Public Data | 6.5/10 | Arcadia case study; thin async |
| Class 3: Geospatial+AI | 8/10 | Best class; peer review innovative |
| Class 4: Energy Modeling | 6.5/10 | Energy Raven case study; 2 broken links |
| Class 5: Hardware Interfaces | 7.5/10 | Osmo/Natel case studies |

### Top 3 Strengths

1. **Exceptional Case Studies** - Every class features compelling real-world examples (Arcadia, SkyTruth, Energy Raven, Osmo Systems, Natel Energy) that show software engineers exactly how their skills apply to climate solutions.

2. **Clear Conceptual Frameworks** - The course introduces memorable mental models: Bits vs Atoms, Raster vs Vector, Access→Synthesize→Act, Electrify Everything + Decarbonize the Grid. These help students organize complex information.

3. **Practical Hands-On Assignments** - Hex notebook assignments apply each week's concepts to real APIs and tools (EIA, Google Earth Engine, pvlib). Students build portfolio-worthy projects.

### Top 3 Areas for Improvement

1. **Broken/Outdated Links** - Multiple async readings link to broken URLs (Drawdown Foundations 403, JP Morgan PDF 404, AIA guide redirect). This frustrates students and undermines trust.

2. **Thin Async Reading** - Classes 1-2 especially provide minimal preparation. Students arrive at live sessions without the conceptual foundation the slides assume.

3. **Metadata/Infrastructure Issues** - All 5 async reading JSON files have wrong `classTitle` ("Emissions, global warming potentials..."). Several Google Docs/Slides returned 401 errors during review.

### Recommended Priority Actions

1. **IMMEDIATE:** Fix all broken links (Drawdown, JP Morgan, AIA, Risk Factor redirect)
2. **SHORT-TERM:** Fix classTitle metadata in all 5 JSON files
3. **MEDIUM-TERM:** Expand async reading for Classes 1-2 with conceptual teasers
4. **ONGOING:** Audit links and resources before each cohort

---

## 2. Course Arc Analysis

### Does the course tell a coherent story?

**YES.** The course follows a logical progression:

```
Week 1: What is Software for Climate? (Landscape)
    ↓
Week 2: How do we access climate data? (Public Data Sources)
    ↓
Week 3: How do we analyze spatial data at scale? (Geospatial + AI)
    ↓
Week 4: How do we model energy systems? (Energy Modeling)
    ↓
Week 5: How does software interact with physical systems? (Hardware Interfaces)
    ↓
Weeks 6-8: Final Project
```

Each class builds on previous concepts. Students go from "why software for climate?" to increasingly technical applications.

### Is the progression logical?

**YES, with minor gaps.** The sequence makes sense:
- Class 1 establishes the "why" and frameworks
- Class 2 introduces data access (foundation for everything)
- Class 3 applies ML to spatial data (builds on data concepts)
- Class 4 models energy systems (applies previous skills to new domain)
- Class 5 bridges software to physical world (capstone before final project)

**Minor gap:** The connection between Classes 2→3 could be more explicit. Both involve data, but the jump to satellite imagery is significant.

### Are there gaps in the narrative?

**MINOR GAPS:**
1. **Data quality/provenance** - Never explicitly addressed. Students learn to access data but not how to evaluate its reliability.
2. **Ethics/limitations** - ML bias, energy costs of AI, measurement uncertainty receive light treatment.
3. **Career paths** - The course focuses on technical skills; guidance on "what jobs exist" is minimal after Class 1.

### Is the "software for climate" theme maintained?

**YES.** Every class connects back to climate impact:
- Class 2: Data enables better climate decisions
- Class 3: Satellite monitoring detects deforestation
- Class 4: Modeling supports decarbonization
- Class 5: IoT enables efficiency improvements

The case studies consistently show climate outcomes, not just technical achievements.

---

## 3. Audience Fit Analysis

### How well does this serve software engineers?

**VERY WELL (8/10).** The course:
- Assumes coding familiarity (appropriate)
- Uses familiar tools (Python, Jupyter/Hex notebooks, APIs)
- Explains domain concepts without requiring prior climate knowledge
- Shows real architectures (Docker, AWS, MQTT, databases)
- Addresses "where can I contribute?" explicitly

**What works:** Frameworks like Bits vs Atoms directly address the "how do I use my skills?" question.

### How well does this serve PMs/designers?

**MODERATELY (6/10).** The course:
- Is code-heavy, which may alienate non-coders
- Provides valuable domain knowledge regardless of role
- Case studies are useful for understanding the landscape
- Assignments require Python familiarity

**Recommendation:** Consider offering non-coding alternatives for some assignments (e.g., analysis write-ups instead of notebooks).

### What assumed knowledge might be missing?

For **software engineers:**
- Basic Python: Addressed in Class 1 with tiered resources
- Climate science: Not required; concepts introduced as needed

For **non-coders:**
- Python basics may not be enough preparation for Hex assignments
- The 1-2 hour Python prep may be optimistic

### What might be too basic for the audience?

**MINOR CONCERNS:**
- "What is an API?" explanations may be redundant for experienced engineers
- Git/version control basics aren't covered (assumed known)
- Some Python basics are explained that experienced devs won't need

The course generally errs on the side of accessibility, which is appropriate for a cohort with mixed backgrounds.

---

## 4. Pedagogical Patterns

### What works well across multiple classes?

1. **Case Study Pattern** - Every class features 1-2 real companies/projects with:
   - Problem statement
   - Solution approach
   - Technical architecture
   - Climate impact
   This pattern is highly effective.

2. **Framework-First Approach** - Introducing mental models (Bits vs Atoms, Raster vs Vector) before diving into details helps students organize information.

3. **Hex Notebook Assignments** - Structured notebooks with scaffolding allow students to learn by doing. The "duplicate and extend" pattern works well.

4. **Optional Q&A Sessions** - Separating core content (60 min) from optional Q&A (30 min) respects students' time while allowing for depth.

### What problems repeat across classes?

1. **Metadata Mismatch** - ALL 5 classes have wrong `classTitle` in JSON files. This is clearly a copy-paste error from an older course (CL101) that was never corrected.

2. **Async Reading Too Thin** - Classes 1, 2, and 4 especially have minimal async content. Learning objectives are stated but not prepared for.

3. **Broken External Links** - 4 major broken links across the course:
   - Class 1: Drawdown Foundations (403)
   - Class 2: Risk Factor redirect
   - Class 4: JP Morgan PDF (404), AIA guide (redirect/broken)

4. **Access Errors** - Multiple X.2 slides and Assignment 5 returned 401 errors during automated fetch. May indicate permission issues.

### Are time estimates consistent and realistic?

**MOSTLY YES.**
- Async reading: Not consistently estimated, but manageable
- Assignments: 1-2 hours is realistic based on scope
- Live sessions: 90 minutes (60 + 30 optional) is well-structured

**Concern:** Assignment 4's two-option format may extend time as students decide.

### Is the async→live→homework pattern effective?

**EFFECTIVE BUT UNDERUTILIZED.**
- The pattern is sound pedagogically
- Async reading often doesn't prepare students for live session concepts
- Homework appropriately applies what's taught
- **Gap:** Async should do more heavy lifting to free up live time for discussion

---

## 5. Consolidated Recommendations

### Must-Fix Issues (Blocking Problems)

| Issue | Location | Fix |
|-------|----------|-----|
| JP Morgan PDF 404 | class-4.json | Update URL to am.jpmorgan.com domain |
| AIA Guide broken | class-4.json | Find new URL or replace with modern resource |
| Drawdown Foundations 403 | class-1-2.json | Change to /solutions |
| Risk Factor redirect | class-2.json | Update to firststreet.org |
| classTitle metadata (ALL) | All 5 JSON files | Change from CL101 title to correct class title |

### Should-Fix Issues (Significant Improvements)

| Issue | Location | Fix |
|-------|----------|-----|
| Thin async reading | Classes 1, 2, 4 | Add conceptual slides before resource links |
| 401 access errors | Slides 4.2, 5.2, Assignment 5 | Verify sharing permissions |
| ACM paper paywall | class-3.json | Note access requirements or provide alternative |
| Decision paralysis (A/B) | Assignment 4 | Add guidance for choosing options |
| Hex invitation expiry | Assignment 1 | Document refresh process |

### Nice-to-Have Improvements

| Issue | Location | Suggestion |
|-------|----------|------------|
| Summary/recap slides | Classes 3, 4, 5 | Add recap of key concepts |
| Deloitte URL redirect | class-5.json | Update to current domain |
| HTTP→HTTPS | Bret Victor link | Minor security improvement |
| Publication dates | Dated resources | Note age of older resources |
| Data quality discussion | Course-wide | Add brief section on evaluating sources |

### Suggested New Content or Restructuring

1. **"Data Quality 101" Mini-Module** - Brief async reading on evaluating data sources, provenance, and limitations.

2. **Non-Coder Track** - For PMs/designers, offer analysis write-ups as assignment alternatives.

3. **Career Paths Appendix** - Expand on "what jobs exist" beyond Class 1 frameworks.

4. **Cross-Class Connections** - Add explicit "Previously..." sections linking each class to prior content.

---

## 6. Final Verdict

### Overall Pedagogical Score: 7.2/10

**Scoring Breakdown:**

| Dimension | Score | Notes |
|-----------|-------|-------|
| Content Quality | 8.5/10 | Excellent frameworks, case studies, technical depth |
| Async Reading | 5.5/10 | Often too thin; multiple broken links |
| Live Session Slides | 9/10 | Consistently excellent |
| Assignments | 8/10 | Practical, achievable, portfolio-worthy |
| Infrastructure | 5/10 | Metadata errors, access issues, broken links |
| Course Arc | 8/10 | Logical progression, clear theme |
| Audience Fit | 7.5/10 | Great for engineers, adequate for PMs |

### Would you recommend this course? To whom?

**YES, with caveats.**

**Strongly Recommended For:**
- Software engineers curious about climate tech
- Developers wanting to transition into climate-focused roles
- Technical PMs with coding background
- Data scientists interested in climate applications

**Recommended With Reservations For:**
- Non-coding PMs/designers (assignments will be challenging)
- Engineers expecting deep technical dives (it's a survey course)
- Those seeking immediate job placement (it's education, not a bootcamp)

**Not Recommended For:**
- Complete programming beginners
- Those expecting climate science depth (it's software-focused)

### What is the single most impactful change?

**Fix the broken links and expand async reading for Classes 1-2.**

The broken links (JP Morgan 404, Drawdown 403) create immediate frustration when students try to follow instructions. This is low-effort/high-impact.

Expanding async reading for Classes 1-2 would transform the course from "slides are great but students arrive unprepared" to "students arrive with foundation, live time is for depth." This is higher effort but would significantly improve learning outcomes.

**If you can only do one thing:** Fix the broken links. It takes 30 minutes and removes the most visible quality issues.

---

## Appendix: Individual Class Scores

| Class | Async | Slides | Assignment | Resources | Alignment | Overall |
|-------|-------|--------|------------|-----------|-----------|---------|
| 1 | 6/10 | 9/10 | 8/10 | 7/10 | 8/10 | **7.5/10** |
| 2 | 4/10 | 8/10 | 7/10 | 7/10 | 7/10 | **6.5/10** |
| 3 | 7/10 | 9/10 | 8/10 | 7/10 | 9/10 | **8/10** |
| 4 | 4/10 | 9/10 | 7/10 | 5/10 | 7/10 | **6.5/10** |
| 5 | 8/10 | 9/10 | N/R | 7/10 | 8/10 | **7.5/10** |

N/R = Not Reviewed (access issues)

---

## Appendix: Complete Broken Links Inventory

| Class | Resource | Current URL | Status | Fix |
|-------|----------|-------------|--------|-----|
| 1 | Drawdown Foundations | drawdown.org/drawdown-foundations | 403 | /solutions |
| 2 | Risk Factor | riskfactor.com | Redirects | firststreet.org |
| 4 | JP Morgan PDF | assets.jpmprivatebank.com/... | 404 | am.jpmorgan.com/... |
| 4 | AIA Guide | content.aia.org/... | Broken redirect | Find new URL |

---

## Appendix: Metadata Fix Summary

All async reading JSON files need `classTitle` field updated:

| File | Current | Correct |
|------|---------|---------|
| class-1-1.json | "Emissions, global warming..." | "1.1 Introductions" |
| class-1-2.json | "Emissions, global warming..." | "1.2 Software x Climate Landscape" |
| class-2.json | "Emissions, global warming..." | "2. Public Data Sources" |
| class-3.json | "Emissions, global warming..." | "3. Geospatial + AI" |
| class-4.json | "Emissions, global warming..." | "4. Energy Modeling" |
| class-5.json | "Emissions, global warming..." | "5. Software/Hardware Interfaces" |
