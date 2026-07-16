# searchpypi.py - Opens several search results

import requests
import sys
import webbrowser
import bs4

print("Searching...")

search_term = " ".join(sys.argv[1:])

res = requests.get(
    "https://html.duckduckgo.com/html/",
    params={"q": search_term},
)

res.raise_for_status()

# Create BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Temporary: inspect the HTML
print(soup.prettify()[:5000])