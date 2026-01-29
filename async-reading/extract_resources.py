#!/usr/bin/env python3
"""Extract all linked resources from course content."""

import json
import re
from pathlib import Path
from html import unescape
from dataclasses import dataclass
from typing import Optional


@dataclass
class Resource:
    url: str
    title: str
    course_id: str
    slide_heading: str
    context: str  # surrounding text
    resource_type: str  # article, tool, dataset, etc.


def classify_resource(url: str, title: str, context: str) -> str:
    """Classify a resource based on URL and context."""
    url_lower = url.lower()
    context_lower = context.lower()
    title_lower = title.lower()

    # Datasets and data sources
    if any(x in url_lower for x in ['epa.gov', 'eia.gov', 'data.', 'dataset', 'api.']):
        return 'dataset'
    if any(x in context_lower for x in ['data source', 'dataset', 'data aggregator']):
        return 'dataset'

    # Tools and platforms
    if any(x in url_lower for x in ['gridstatus', 'riskfactor', 'climatetechlist', 'app.', 'tool']):
        return 'tool'
    if any(x in context_lower for x in ['tool', 'platform', 'app', 'calculator']):
        return 'tool'

    # Documentation and guides
    if any(x in url_lower for x in ['docs.', 'documentation', 'guide', 'tutorial']):
        return 'documentation'

    # GitHub repos
    if 'github.com' in url_lower:
        return 'repository'

    # Videos
    if any(x in url_lower for x in ['youtube', 'vimeo', 'video']):
        return 'video'

    # Default to article
    return 'article'


def extract_links_from_html(html: str) -> list[tuple[str, str]]:
    """Extract (url, title) pairs from HTML."""
    pattern = r'<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>'
    matches = re.findall(pattern, html)
    return [(url, unescape(title.strip())) for url, title in matches if url.startswith('http')]


def extract_resources_from_course(json_path: Path) -> list[Resource]:
    """Extract all resources from a course JSON file."""
    with open(json_path) as f:
        data = json.load(f)

    course_id = data.get('id', 'unknown')
    resources = []

    for slide in data.get('content', []):
        slide_heading = slide.get('slideHeading', 'Unknown')
        body_parts = slide.get('body', [])

        for part in body_parts:
            links = extract_links_from_html(part)
            for url, title in links:
                # Get surrounding context (strip HTML for readability)
                context = re.sub(r'<[^>]+>', ' ', part)
                context = unescape(context)
                context = ' '.join(context.split())[:200]  # First 200 chars

                resource_type = classify_resource(url, title, context)

                resources.append(Resource(
                    url=url,
                    title=title or url,
                    course_id=course_id,
                    slide_heading=slide_heading,
                    context=context,
                    resource_type=resource_type
                ))

    return resources


def generate_index(resources: list[Resource]) -> str:
    """Generate markdown index from resources."""
    lines = [
        "# Resource Index",
        "",
        "All external resources referenced in the SFC async reading materials.",
        "",
        f"**Total resources:** {len(resources)}",
        "",
    ]

    # Group by resource type
    by_type: dict[str, list[Resource]] = {}
    for r in resources:
        by_type.setdefault(r.resource_type, []).append(r)

    type_order = ['dataset', 'tool', 'repository', 'article', 'documentation', 'video']
    type_labels = {
        'dataset': 'Datasets & Data Sources',
        'tool': 'Tools & Platforms',
        'repository': 'Code Repositories',
        'article': 'Articles & Reading',
        'documentation': 'Documentation & Guides',
        'video': 'Videos'
    }

    for rtype in type_order:
        if rtype not in by_type:
            continue

        lines.append(f"## {type_labels.get(rtype, rtype.title())}")
        lines.append("")

        for r in by_type[rtype]:
            lines.append(f"### [{r.title}]({r.url})")
            lines.append("")
            lines.append(f"- **Course:** `{r.course_id}`")
            lines.append(f"- **Section:** {r.slide_heading}")
            lines.append(f"- **Type:** {r.resource_type}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Also create a flat list for easy link checking
    lines.append("## All URLs (for link checking)")
    lines.append("")
    lines.append("```")
    seen = set()
    for r in resources:
        if r.url not in seen:
            lines.append(r.url)
            seen.add(r.url)
    lines.append("```")

    return '\n'.join(lines)


def main():
    async_dir = Path(__file__).parent

    all_resources = []
    for json_file in sorted(async_dir.glob('class-*.json')):
        print(f"Extracting from {json_file.name}...")
        resources = extract_resources_from_course(json_file)
        all_resources.extend(resources)
        print(f"  Found {len(resources)} resources")

    print(f"\nTotal: {len(all_resources)} resources")

    index_content = generate_index(all_resources)
    index_path = async_dir / 'RESOURCE_INDEX.md'
    index_path.write_text(index_content)
    print(f"\nWrote {index_path}")


if __name__ == '__main__':
    main()
