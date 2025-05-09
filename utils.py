streamable_movie_bot/utils.py

import requests from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

List of websites to search

SITES = [ "https://vegamovies.dad", "https://moviesmod.skin", "https://bollyflix.run", "https://moviemad.world", "https://hdhub4u.wiki" ]

STREAM_KEYWORDS = ["drive.google.com", "dood", "streamtape"]

def scrape_stream_link(query): search_path = "/?s=" + query.replace(" ", "+")

for base_url in SITES:
    try:
        print(f"Searching in: {base_url}")
        search_url = base_url + search_path
        res = requests.get(search_url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        result_link = soup.select_one("h2.entry-title a")
        if not result_link:
            continue

        movie_url = result_link['href']
        print(f"Opening movie page: {movie_url}")
        page = requests.get(movie_url, headers=HEADERS, timeout=10)
        page_soup = BeautifulSoup(page.text, "html.parser")

        all_links = page_soup.select("a[href]")
        for link in all_links:
            href = link.get("href")
            if any(key in href for key in STREAM_KEYWORDS):
                return href

    except Exception as e:
        print(f"Error while scraping {base_url}: {e}")
        continue

return None

