# app/services/data_service.py

import requests

def get_market_data(sector: str):
    try:
        query = f"{sector} sector India market trends news"
        url = f"https://api.duckduckgo.com/?q={query}&format=json"

        response = requests.get(url)

        if response.status_code != 200:
            return f"No live data found for {sector}"

        data = response.json()

        # extract useful text
        related = data.get("RelatedTopics", [])
        snippets = []

        for item in related[:5]:
            if "Text" in item:
                snippets.append(item["Text"])

        return " ".join(snippets) if snippets else f"No detailed data for {sector}"

    except Exception:
        return f"Error fetching data for {sector}"