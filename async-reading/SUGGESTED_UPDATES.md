# Suggested Updates for SFC Async Reading

Review completed: 2026-01-28

## Summary

- **Total resources reviewed:** 24
- **Broken/inaccessible links:** 3
- **Suggested replacements:** 3
- **Potential new resources:** 8

---

## Broken Links (Action Required)

### 1. Project Drawdown Foundations
- **Current URL:** https://drawdown.org/drawdown-foundations
- **Issue:** Returns 403 Forbidden (may be blocking automated requests)
- **Status:** URL appears valid in browser, may just need manual verification
- **Recommendation:** Test manually; if still broken, the content is now part of [Drawdown Explorer](https://drawdown.org/news/project-drawdown-launches-drawdown-explorer-the-worlds-most-comprehensive-climate-solutions)
- **Course:** software-for-climate-1-2

### 2. EIA Hourly Electric Grid Monitor
- **Current URL:** https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48
- **Issue:** Connection timeout
- **Replacement:** https://www.eia.gov/electricity/gridmonitor/dashboard/daily_generation_mix/US48/US48
- **Note:** EIA has redesigned the dashboard; the new URL structure uses `daily_generation_mix` instead of `electric_overview`
- **Course:** software-for-climate-2

### 3. JP Morgan "Growing Pains" PDF
- **Current URL:** https://assets.jpmprivatebank.com/content/dam/jpm-wm-aem/campaign/energy-paper-13/growing-pains-renewable-transition-in-adolescence.pdf
- **Issue:** 404 Not Found
- **Replacement:** https://am.jpmorgan.com/content/dam/jpm-am-aem/global/campaign/energy-paper-13/growing-pains-renewable-transition-in-adolescence.pdf
- **Alternative:** https://privatebank.jpmorgan.com/content/dam/jpm-wm-aem/global/cwm/en/insights/eye-on-the-market/2023-annual-energy-paper-jpmwm.pdf
- **Note:** PDF moved to different JP Morgan subdomain
- **Course:** software-for-climate-4

---

## Resources That May Be Outdated

### 1. Bret Victor's "What can a technologist do about climate change?"
- **Current URL:** http://worrydream.com/ClimateChange
- **Issue:** Article is from 2015 - over 10 years old
- **Status:** Still valuable as foundational reading, but climate tech landscape has changed dramatically
- **Recommendation:** Keep but supplement with more recent overview
- **Suggested addition:** [MIT Technology Review - Three climate technologies breaking through in 2026](https://www.technologyreview.com/2026/01/15/1131348/climate-technologies-2026)
- **Course:** software-for-climate-1-2

### 2. AIA Energy Modeling Guide
- **Current URL:** https://content.aia.org/sites/default/files/2016-04/Energy-Modeling-Design-Process-Guide.pdf
- **Issue:** From 2016 - 10 years old
- **Status:** Principles still valid but tools have evolved
- **Recommended addition:** [ClimateStudio](https://www.solemma.com/climatestudio) as modern alternative, or [IEA Global Energy and Climate Model Documentation 2025](https://powerlibrary.theelectricityhub.com/2025/12/10/global-energy-and-climate-model-documentation-2025-iea/)
- **Course:** software-for-climate-4

### 3. Deloitte Industry 4.0 Paper
- **Current URL:** https://www2.deloitte.com/content/dam/insights/us/articles/manufacturing-ecosystems-exploring-world-connected-enterprises/DUP_2898_Industry4.0ManufacturingEcosystems.pdf
- **Issue:** Pre-2020 publication
- **Status:** Foundational concepts still relevant
- **Recommendation:** Consider supplementing with more recent Industry 4.0/5.0 resources
- **Course:** software-for-climate-5

---

## Suggested New Resources by Topic

### Class 1-2: Software x Climate Landscape
| Resource | Type | Rationale |
|----------|------|-----------|
| [10 Top Climate Tech Startups to Watch in 2026](https://www.startus-insights.com/innovators-guide/top-climate-tech-startups/) | Article | Current landscape of funded climate tech |
| [Y Combinator Climate Startups 2026](https://www.ycombinator.com/companies/industry/climate) | Directory | Real-world examples of software in climate |
| [Watershed Platform](https://watershed.com/) | Tool | Enterprise sustainability platform example |

### Class 2: Public Data Sources
| Resource | Type | Rationale |
|----------|------|-----------|
| [Carbon Mapper](https://carbonmapper.org/) | Tool | Satellite-based methane/CO2 detection |
| [GHGSat](https://www.ghgsat.com/) | Tool | Commercial methane monitoring constellation |

### Class 3: Geospatial + AI
| Resource | Type | Rationale |
|----------|------|-----------|
| [Global methane leak map from satellites (2025)](https://phys.org/news/2025-12-global-fleet-satellites-methane-leaks.html) | Article | First-ever global map of industrial methane leaks |
| [Vision transformer for methane detection (Nature 2024)](https://www.nature.com/articles/s41467-024-47754-y) | Paper | State-of-the-art ML for satellite imagery |
| [AWS SageMaker Geospatial for methane monitoring](https://aws.amazon.com/blogs/machine-learning/detection-and-high-frequency-monitoring-of-methane-emission-point-sources-using-amazon-sagemaker-geospatial-capabilities/) | Tutorial | Practical implementation guide |

### Class 4: Energy Modeling
| Resource | Type | Rationale |
|----------|------|-----------|
| [LEAP - Low Emissions Analysis Platform](https://www.sei.org/tools/leap/) | Tool | Free energy/climate modeling tool for 146 countries |
| [NEMO Energy Modeling System](https://www.sei.org/tools/nemo-the-next-energy-modeling-system-for-optimization/) | Tool | Modern optimization-based energy modeling |
| [ClimateStudio](https://www.solemma.com/climatestudio) | Tool | Building energy modeling software |

### Class 5: Software/Hardware Interfaces
| Resource | Type | Rationale |
|----------|------|-----------|
| [Renewable Energy Software Trends 2026](https://tech-stack.com/blog/the-future-of-renewable-energy-software/) | Article | AI, digital twins, smart grids overview |

---

## Action Items

1. **Immediate:** Fix the 3 broken links listed above
2. **Review:** Manually verify Drawdown Foundations URL in browser
3. **Consider:** Adding 2-3 new resources per class to keep content current
4. **Optional:** Add publication dates to existing resources so staleness is visible

---

## Link Check Results

Full automated link check results saved to: `link_check_results.json`

### Summary
- ✅ 21 URLs accessible
- ⚠️ 7 URLs redirected (but working)
- ❌ 3 URLs broken or inaccessible
