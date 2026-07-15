# searchpypi.py - Opens several search results on pypi.org

import requests
import sys
import webbrowser
import bs4

print("Searching...")

res = requests.get(
    "https://pypi.org/search/?q=" + " ".join(sys.argv[1:])
)
res.raise_for_status()

# TODO: Retrieve top search result links.

# TODO: Open a browser tab for each result.