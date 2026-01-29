#!/usr/bin/env python3
"""Check all resource URLs for validity."""

import urllib.request
import urllib.error
import ssl
from pathlib import Path
import json
import time

# URLs from RESOURCE_INDEX.md
URLS = [
    "https://hex.tech/blog/beginners-guide-to-python-notebooks/",
    "https://speedandscale.com/tracker/",
    "https://drawdown.org/drawdown-foundations",
    "https://drawdown.org/sectors",
    "https://www.climatepapa.com/software",
    "https://www.climatetechlist.com/blog/bits-vs-atoms-framework",
    "http://worrydream.com/ClimateChange",
    "https://www.epa.gov/egrid/power-profiler#/",
    "https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48",
    "https://www.gridstatus.io/",
    "https://climatetechlist.com/charts",
    "https://riskfactor.com/",
    "https://www.ctvc.co/inside-methane-monitorings-big-moment/",
    "https://www.maaproject.org/maap-212-machine-learning-to-detect-mining-deforestation-across-the-amazon/",
    "https://blog.google/outreach-initiatives/sustainability/how-satellites-algorithms-and-ai-can-help-map-and-trace-methane-sources/",
    "https://climate.benjames.io/ai-go-brrr/",
    "https://assets.jpmprivatebank.com/content/dam/jpm-wm-aem/campaign/energy-paper-13/growing-pains-renewable-transition-in-adolescence.pdf",
    "https://www.volts.wtf/p/whats-the-deal-with-interconnection",
    "https://content.aia.org/sites/default/files/2016-04/Energy-Modeling-Design-Process-Guide.pdf",
    "https://redeem-tomorrow.com/if-you-can-use-open-source-you-can-build-hardware",
    "https://www2.deloitte.com/content/dam/insights/us/articles/manufacturing-ecosystems-exploring-world-connected-enterprises/DUP_2898_Industry4.0ManufacturingEcosystems.pdf",
    "https://excelpro.ca/en/news/the-automation-pyramid-isa-95",
    "https://www.reddit.com/r/PLC/comments/2a5g4q/comment/ciry1u2/",
    "https://www.solisplc.com/tutorials/how-to-read-ladder-logic",
]


def check_url(url: str, timeout: int = 10) -> dict:
    """Check if URL is accessible."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, timeout=timeout, context=ctx)
        return {
            "url": url,
            "status": response.status,
            "ok": True,
            "final_url": response.url,
            "redirected": response.url != url
        }
    except urllib.error.HTTPError as e:
        return {
            "url": url,
            "status": e.code,
            "ok": False,
            "error": str(e.reason)
        }
    except urllib.error.URLError as e:
        return {
            "url": url,
            "status": None,
            "ok": False,
            "error": str(e.reason)
        }
    except Exception as e:
        return {
            "url": url,
            "status": None,
            "ok": False,
            "error": str(e)
        }


def main():
    results = []

    for i, url in enumerate(URLS):
        print(f"[{i+1}/{len(URLS)}] Checking {url[:60]}...")
        result = check_url(url)
        results.append(result)

        if result["ok"]:
            status = "✓" if not result.get("redirected") else "→ redirected"
            print(f"  {status}")
        else:
            print(f"  ✗ {result.get('error', 'Unknown error')}")

        time.sleep(0.5)  # Be polite

    # Summary
    ok_count = sum(1 for r in results if r["ok"])
    print(f"\n{'='*50}")
    print(f"Results: {ok_count}/{len(results)} URLs accessible")

    broken = [r for r in results if not r["ok"]]
    if broken:
        print(f"\nBroken/inaccessible links:")
        for r in broken:
            print(f"  - {r['url']}")
            print(f"    Error: {r.get('error', 'Unknown')}")

    # Save results
    output_path = Path(__file__).parent / "link_check_results.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
