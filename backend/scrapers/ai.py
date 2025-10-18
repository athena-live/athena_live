import json
from textwrap import dedent


def generate_scraper_code(url: str, company: str) -> str:
    """
    Return a simple Python script stub that prints JSON output.

    This keeps the code generator deterministic for now; replace with real AI
    integration when available.
    """
    payload = {
        "company": company,
        "url": url,
        "results": [],
    }

    script = f"""
import json


def main():
    data = {json.dumps(payload, indent=4)}
    print(json.dumps(data))


if __name__ == "__main__":
    main()
"""
    return dedent(script)
