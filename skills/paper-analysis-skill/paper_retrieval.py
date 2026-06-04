import requests
import feedparser

ARXIV_API = "http://export.arxiv.org/api/query"

def search_papers(query: str, k: int = 5):

    print(f"[arXiv] query = {query}")

    url = f"{ARXIV_API}?search_query=all:{query}&start=0&max_results={k}"

    response = requests.get(url)
    feed = feedparser.parse(response.text)

    pdf_files = []

    for i, entry in enumerate(feed.entries):

        title = entry.title
        pdf_url = entry.links[1].href

        print(f"[Download] {title}")

        r = requests.get(pdf_url, headers={
            "User-Agent": "Mozilla/5.0"
        })

        filename = f"paper_{i}.pdf"

        with open(filename, "wb") as f:
            f.write(r.content)

        pdf_files.append(filename)

    return pdf_files