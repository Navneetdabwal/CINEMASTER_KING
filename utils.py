import requests
from bs4 import BeautifulSoup

def scrape_stream_link(query):
    base_url = "https://vegamovies.dad"
    search_url = f"{base_url}/?s={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        first = soup.select_one("h2.entry-title a")
        if not first:
            return None

        movie_page = requests.get(first['href'], headers=headers)
        movie_soup = BeautifulSoup(movie_page.text, "html.parser")

        links = movie_soup.select("a")
        for link in links:
            href = link.get("href")
            if href and ("drive.google.com" in href or "dood" in href or "streamtape" in href):
                return href
    except:
        pass

    return None