#!/usr/bin/env python3
"""Explore and document Google Drive folder structure for SFC course materials."""

import json
import os
from pathlib import Path
from typing import Any

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Folder IDs from the URLs
ASSIGNMENTS_FOLDER_ID = "1tFEIkdHjjIZ_3h5jcvx-0qzpAkvCJgYZ"
LIVE_SESSIONS_FOLDER_ID = "1dsUc8YSBKRjMwFpNGa0gxsfsBSvFJmrK"

# Default service account key path
DEFAULT_KEY_PATH = os.path.expanduser(
    "~/code/sfc-course-materials/sfc-internal-tools-56e7e040f221.json"
)


def get_drive_service(key_path: str = DEFAULT_KEY_PATH):
    """Create authenticated Google Drive service."""
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/drive.readonly"]
    )
    return build("drive", "v3", credentials=credentials)


def list_folder_contents(
    service, folder_id: str, parent_path: str = ""
) -> list[dict[str, Any]]:
    """Recursively list all contents of a folder."""
    items = []
    page_token = None

    while True:
        response = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed=false",
                spaces="drive",
                fields="nextPageToken, files(id, name, mimeType, modifiedTime, webViewLink)",
                pageToken=page_token,
            )
            .execute()
        )

        for file in response.get("files", []):
            item = {
                "id": file["id"],
                "name": file["name"],
                "mimeType": file["mimeType"],
                "modifiedTime": file.get("modifiedTime", ""),
                "webViewLink": file.get("webViewLink", ""),
                "path": f"{parent_path}/{file['name']}" if parent_path else file["name"],
            }

            # If it's a folder, recurse into it
            if file["mimeType"] == "application/vnd.google-apps.folder":
                item["type"] = "folder"
                item["children"] = list_folder_contents(
                    service, file["id"], item["path"]
                )
            else:
                item["type"] = "file"
                # Map Google MIME types to readable names
                mime_map = {
                    "application/vnd.google-apps.document": "Google Doc",
                    "application/vnd.google-apps.spreadsheet": "Google Sheet",
                    "application/vnd.google-apps.presentation": "Google Slides",
                    "application/vnd.google-apps.form": "Google Form",
                    "application/pdf": "PDF",
                }
                item["fileType"] = mime_map.get(file["mimeType"], file["mimeType"])

            items.append(item)

        page_token = response.get("nextPageToken")
        if not page_token:
            break

    # Sort: folders first, then by name
    items.sort(key=lambda x: (x["type"] != "folder", x["name"].lower()))
    return items


def format_tree(items: list[dict], indent: int = 0) -> str:
    """Format folder structure as a tree string."""
    lines = []
    prefix = "  " * indent

    for item in items:
        if item["type"] == "folder":
            lines.append(f"{prefix}📁 {item['name']}/")
            if item.get("children"):
                lines.append(format_tree(item["children"], indent + 1))
        else:
            icon = {
                "Google Doc": "📄",
                "Google Sheet": "📊",
                "Google Slides": "📽️",
                "Google Form": "📝",
                "PDF": "📑",
            }.get(item.get("fileType", ""), "📄")
            lines.append(f"{prefix}{icon} {item['name']} ({item.get('fileType', 'file')})")

    return "\n".join(lines)


def count_items(items: list[dict]) -> dict[str, int]:
    """Count items by type."""
    counts = {"folders": 0, "files": 0, "docs": 0, "slides": 0, "sheets": 0, "other": 0}

    for item in items:
        if item["type"] == "folder":
            counts["folders"] += 1
            if item.get("children"):
                child_counts = count_items(item["children"])
                for k, v in child_counts.items():
                    counts[k] += v
        else:
            counts["files"] += 1
            file_type = item.get("fileType", "")
            if "Doc" in file_type:
                counts["docs"] += 1
            elif "Slides" in file_type or "Presentation" in file_type:
                counts["slides"] += 1
            elif "Sheet" in file_type:
                counts["sheets"] += 1
            else:
                counts["other"] += 1

    return counts


def explore_folders(key_path: str = DEFAULT_KEY_PATH) -> dict[str, Any]:
    """Explore both folders and return structured data."""
    service = get_drive_service(key_path)

    results = {
        "assignments": {
            "folder_id": ASSIGNMENTS_FOLDER_ID,
            "url": f"https://drive.google.com/drive/folders/{ASSIGNMENTS_FOLDER_ID}",
            "contents": list_folder_contents(service, ASSIGNMENTS_FOLDER_ID),
        },
        "live_sessions": {
            "folder_id": LIVE_SESSIONS_FOLDER_ID,
            "url": f"https://drive.google.com/drive/folders/{LIVE_SESSIONS_FOLDER_ID}",
            "contents": list_folder_contents(service, LIVE_SESSIONS_FOLDER_ID),
        },
    }

    # Add counts
    results["assignments"]["counts"] = count_items(results["assignments"]["contents"])
    results["live_sessions"]["counts"] = count_items(results["live_sessions"]["contents"])

    return results


def generate_report(results: dict[str, Any]) -> str:
    """Generate a markdown report of the folder structure."""
    report = []
    report.append("# Google Drive Folder Structure Report")
    report.append("")
    report.append("## Summary")
    report.append("")

    for name, data in [("Assignments", results["assignments"]), ("Live Sessions Slides", results["live_sessions"])]:
        counts = data["counts"]
        report.append(f"### {name}")
        report.append(f"- **URL**: {data['url']}")
        report.append(f"- **Total folders**: {counts['folders']}")
        report.append(f"- **Total files**: {counts['files']}")
        report.append(f"  - Google Docs: {counts['docs']}")
        report.append(f"  - Google Slides: {counts['slides']}")
        report.append(f"  - Google Sheets: {counts['sheets']}")
        report.append(f"  - Other: {counts['other']}")
        report.append("")

    report.append("## Detailed Structure")
    report.append("")

    report.append("### Assignments Folder")
    report.append("```")
    report.append(format_tree(results["assignments"]["contents"]))
    report.append("```")
    report.append("")

    report.append("### Live Sessions Slides Folder")
    report.append("```")
    report.append(format_tree(results["live_sessions"]["contents"]))
    report.append("```")

    return "\n".join(report)


if __name__ == "__main__":
    import sys

    key_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_KEY_PATH

    print(f"Using service account key: {key_path}")
    print("Exploring Google Drive folders...")

    results = explore_folders(key_path)

    # Save raw JSON data
    output_dir = Path(__file__).parent.parent.parent
    json_path = output_dir / "gdrive_structure.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved JSON data to: {json_path}")

    # Generate and save markdown report
    report = generate_report(results)
    report_path = output_dir / "GDRIVE_STRUCTURE.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Saved report to: {report_path}")

    # Print summary
    print("\n" + "=" * 60)
    print(report)
