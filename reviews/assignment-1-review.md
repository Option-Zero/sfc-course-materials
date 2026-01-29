# Assignment 1 Review: Introductions & Software x Climate

**Reviewer**: Polecat nux
**Date**: 2026-01-28
**Documents Reviewed**:
- Assignment 1 Google Doc (1ctU3feDrumYTUP5_dX5ulM6fRmjzlg2Pe3cEBtG96UU)
- Slides 1.1 Introductions
- Slides 1.2 Software x Climate Landscape
- async-reading/class-1-1.md & class-1-1.json
- async-reading/class-1-2.md

---

## Summary

Overall, the assignment aligns well with the course slides and async reading materials. I identified several issues requiring attention, primarily around broken links and outdated references.

---

## Issues Found

### 1. BROKEN LINK - Python Cheatsheet (HIGH PRIORITY)

**Location**: class-1-1.json (slideId 4), referenced in async reading
**Current URL**: `https://www.pythoncheatsheet.org/cheatsheet/basics`
**Status**: Returns 301 redirect to labex.io, which then returns 403 Forbidden
**Recommendation**: Replace with working alternative such as:
- https://www.pythoncheatsheet.org/ (main site may still work)
- https://docs.python.org/3/library/index.html
- https://quickref.me/python.html

---

### 2. OUTDATED REFERENCE - Convoy (MEDIUM PRIORITY)

**Location**: Slides 1.1 Introductions
**Issue**: Convoy is mentioned as a "climate-focused unicorn" in instructor backgrounds
**Reality**: Convoy shut down operations in October 2023 after running out of funding. The company no longer exists.
**Recommendation**: Update to either:
- Remove the reference entirely
- Note it as a past experience: "...including Convoy (freight optimization, 2019-2023)..."
- Replace with a current climate tech example

---

### 3. TYPO - "lecutures" (LOW PRIORITY)

**Location**: async-reading/class-1-1.md, line 32
**Current**: "involving lecutures, audience participation"
**Correct**: "involving **lectures**, audience participation"

---

### 4. METADATA MISMATCH (LOW PRIORITY)

**Location**: async-reading/class-1-1.json
**Issue**: The `classTitle` field says "Emissions, global warming potentials and the global carbon cycle" but the actual content is "1.1 Introductions"
**Recommendation**: Update classTitle to "1.1 Introductions" or "Software for Climate - Introductions"

---

### 5. MARKDOWN MISSING HYPERLINKS (MEDIUM PRIORITY)

**Location**: async-reading/class-1-1.md, Reading section (lines 103-117)
**Issue**: Resource links are shown as plain text instead of clickable markdown links
**Current**:
```
- Python cheat sheet & quick reference
- Python tutorial (free) - chapters 3 & 4 are the most relevant
```
**Should be**:
```
- [Python cheat sheet & quick reference](https://www.pythoncheatsheet.org/cheatsheet/basics)
- [Python tutorial (free)](https://docs.python.org/3/tutorial/introduction.html) - chapters 3 & 4 are the most relevant
```
**Note**: The JSON file has the correct URLs; they just need to be rendered properly in the markdown

---

### 6. COHORT-SPECIFIC DUE DATE (INFO)

**Location**: Assignment 1 Google Doc
**Current**: "Friday, October 3, 9:00 AM PT"
**Note**: This date needs to be updated for each new cohort. Consider using a relative date like "Friday of Week 1" or maintaining a separate schedule document.

---

### 7. HARDWARE PRICING VERIFICATION NEEDED (LOW PRIORITY)

**Location**: Assignment 1 Google Doc
**Current**: IoT components ranging from $45.80 (minimum) to $147.55 (expanded)
**Note**: IoT component prices fluctuate significantly. Verify these prices are still accurate before each cohort starts, or provide links to current pricing pages rather than fixed dollar amounts.

---

## Working Links Verified

The following resource links were verified as working:
- Speed and Scale Tracker (speedandscale.com/tracker/) - Updated April/September 2025
- Project Drawdown Sectors (drawdown.org/sectors) - Accessible
- Climate Papa Software Guide (climatepapa.com/software) - Working
- Bits vs Atoms Framework (climatetechlist.com/blog/bits-vs-atoms-framework) - Working
- Bret Victor Article (worrydream.com/ClimateChange) - Working
- Hex Notebooks Guide (hex.tech/blog/beginners-guide-to-python-notebooks/) - Working
- Python Official Tutorial (docs.python.org/3/tutorial/introduction.html) - Working
- Codecademy Python Course (codecademy.com/enrolled/courses/learn-python-3) - Working

---

## Alignment Assessment

### Assignment <-> Slides Alignment: GOOD
- Assignment tasks (Slack, Airtable, Hex, climate company research) align with course objectives
- The "identify 3-5 climate tech companies" task connects directly to the Bits vs Atoms framework in slides 1.2

### Assignment <-> Async Reading Alignment: GOOD
- Both emphasize the three learning components (async reading, live sessions, homework)
- Python preparation resources are consistent
- Hex notebooks are properly introduced

---

## Recommended Priority Order

1. **HIGH**: Fix Python cheatsheet broken link (blocks student preparation)
2. **MEDIUM**: Update Convoy reference (outdated/misleading)
3. **MEDIUM**: Add proper markdown links to class-1-1.md
4. **LOW**: Fix "lecutures" typo
5. **LOW**: Fix classTitle metadata
6. **INFO**: Document process for updating cohort-specific dates and prices
