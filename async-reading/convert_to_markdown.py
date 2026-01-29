#!/usr/bin/env python3
"""Convert Terra.do course JSON to markdown."""

import json
import re
from pathlib import Path
from html import unescape

def html_to_markdown(html: str) -> str:
    """Simple HTML to markdown conversion."""
    if not html or html.strip() == " ":
        return ""

    text = html

    # Handle divs and paragraphs
    text = re.sub(r'<div[^>]*>', '\n', text)
    text = re.sub(r'</div>', '', text)
    text = re.sub(r'<p[^>]*>', '\n', text)
    text = re.sub(r'</p>', '', text)

    # Handle lists
    text = re.sub(r'<ul[^>]*>', '\n', text)
    text = re.sub(r'</ul>', '\n', text)
    text = re.sub(r'<ol[^>]*>', '\n', text)
    text = re.sub(r'</ol>', '\n', text)
    text = re.sub(r'<li[^>]*>', '- ', text)
    text = re.sub(r'</li>', '\n', text)

    # Handle links
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', text)

    # Handle formatting
    text = re.sub(r'<strong>([^<]*)</strong>', r'**\1**', text)
    text = re.sub(r'<b>([^<]*)</b>', r'**\1**', text)
    text = re.sub(r'<em>([^<]*)</em>', r'*\1*', text)
    text = re.sub(r'<i>([^<]*)</i>', r'*\1*', text)

    # Handle breaks and spaces
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = unescape(text)

    # Remove remaining tags
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def convert_course(json_path: Path) -> str:
    """Convert a course JSON file to markdown."""
    with open(json_path) as f:
        data = json.load(f)

    course_id = data.get('id', 'unknown')

    # Get actual title from first slide body
    first_slide = data.get('content', [{}])[0]
    body_preview = html_to_markdown('\n'.join(first_slide.get('body', [])))
    title_match = re.search(r'(\d+\.?\d*\.?\s+.+)', body_preview)
    title = title_match.group(1) if title_match else first_slide.get('slideHeading', course_id)

    lines = [
        f"# {title}",
        "",
        f"**Course ID:** `{course_id}`",
        "",
    ]

    # Add index/TOC if available
    index = data.get('index', [])
    if index:
        lines.append("## Contents")
        lines.append("")
        for item in index:
            lines.append(f"- {item.get('heading', 'Unknown')}")
        lines.append("")

    # Process each slide
    lines.append("---")
    lines.append("")

    for slide in data.get('content', []):
        slide_id = slide.get('slideId', '')
        heading = slide.get('slideHeading', 'Untitled')
        body_parts = slide.get('body', [])

        # Skip template/placeholder slides
        if heading in ['Thankyou slide', 'End of Section 1', 'Section break!']:
            continue

        lines.append(f"## {heading}")
        lines.append("")

        for part in body_parts:
            md = html_to_markdown(part)
            if md:
                lines.append(md)
                lines.append("")

        # Add multimedia if present
        multimedia = slide.get('multimedia', '').strip()
        if multimedia and multimedia != ' ':
            lines.append(f"![{slide.get('multimediaTitle', 'Image')}]({multimedia})")
            lines.append("")

        lines.append("---")
        lines.append("")

    return '\n'.join(lines)


def main():
    async_dir = Path(__file__).parent

    for json_file in sorted(async_dir.glob('class-*.json')):
        print(f"Converting {json_file.name}...")
        md_content = convert_course(json_file)

        md_file = json_file.with_suffix('.md')
        md_file.write_text(md_content)
        print(f"  -> {md_file.name}")


if __name__ == '__main__':
    main()
