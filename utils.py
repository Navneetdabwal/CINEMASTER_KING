import requests
from bs4 import BeautifulSoup

def search_movie_links(query):
    try:
        search_url = f"https://duckduckgo.com/html/?q=site:drive.google.com+{query.replace(' ', '+')}+filetype:mp4"
        headers = {"User-Agent": "Mozilla/5.0"}

        res = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.select("a.result__a")

        for link in results:
            href = link.get("href")
            if href and "drive.google.com" in href:
                return href

        return None
    except Exception as e:
        print("Search error:", e)
        return None
