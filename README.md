# sfc-course-materials

Private course materials for the [Terra.do Software for Climate](https://www.terra.do/climate-change-courses/software-for-climate/) course. This repository backs up course content and manages resource freshness.

## Contents

- **`/async-reading/`** - Terra.do app course content
  - `class-*.json` - Raw course data from Terra.do API
  - `class-*.md` - Human-readable markdown versions
  - `RESOURCE_INDEX.md` - Index of all external resources (24 links)
  - `SUGGESTED_UPDATES.md` - Link check results and update recommendations
  - Scripts: `fetch_courses.sh`, `convert_to_markdown.py`, `extract_resources.py`, `check_links.py`

## Setup

This project uses [UV](https://docs.astral.sh/uv/) for Python environment management.

```bash
# Install dependencies
uv sync

# Run scripts
uv run python async-reading/check_links.py
```

### Google Drive API

Course content fetching requires Google Drive API access via service account. Place credentials at the expected path or configure via environment variables.
