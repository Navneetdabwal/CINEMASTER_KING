from googlesearch import search

def search_google_link(query):
    keywords = ["drive.google.com", "dood", "streamtape", "telegraph"]
    try:
        results = search(query + " " + " OR ".join(keywords), num_results=10)
        for link in results:
            if any(k in link for k in keywords):
                return link
    except Exception as e:
        print("Google search error:", e)
    return None
    
