# Search PyPI Automation Script

## Description

This project is based on **Project 7: Open All Search Results** from the book:

**Automate the Boring Stuff with Python**

The purpose of this project is to automate the process of searching the Python Package Index (PyPI) and opening multiple search results in browser tabs.

The program is designed to:

1. Accept search keywords from the command line.
2. Retrieve the PyPI search results page.
3. Parse the HTML using Beautiful Soup.
4. Find search result links.
5. Automatically open the results in a web browser.

Example:

```bash
python searchpypi.py requests
```

---

## Features

- Accepts search terms through command-line arguments.
- Uses Python's `requests` module to retrieve web pages.
- Uses Beautiful Soup to parse HTML.
- Extracts links from search results.
- Opens multiple browser tabs automatically.

---

## Technologies Used

- Python 3
- Requests
- Beautiful Soup 4
- Webbrowser module
- Command-line arguments (`sys.argv`)

---

## How It Works

### 1. User Provides Search Terms

The program reads search keywords from the command line using:

```python
sys.argv
```

Example:

```bash
python searchpypi.py flask
```

The program combines the arguments into a search query.

---

### 2. Retrieve Search Results

The script sends a request to the PyPI search page using the Requests library:

```python
requests.get()
```

The returned HTML is then passed to Beautiful Soup for processing.

---

### 3. Parse HTML With Beautiful Soup

Beautiful Soup creates a searchable representation of the HTML:

```python
BeautifulSoup()
```

The program searches for result links using CSS selectors:

```python
soup.select()
```

---

### 4. Open Results Automatically

The script opens each result in a new browser tab using:

```python
webbrowser.open()
```

This removes the need to manually open multiple search results.

---

# Disclaimer: Website Changes and Web Scraping Limitations

This project follows the original implementation from **Automate the Boring Stuff with Python**.

However, websites change over time, and modern websites often use security measures to prevent automated scraping.

The original PyPI scraping method from the book no longer works reliably because:

- PyPI has changed its HTML structure since the book was written.
- The original CSS selector (`.package-snippet`) is no longer used.
- Automated HTTP requests may receive security verification pages instead of the actual search results.
- Additional browser automation tools would be required to interact with the current PyPI website.

This repository is preserved as a learning project to demonstrate the concepts behind web scraping and browser automation.

The project demonstrates:

- Sending HTTP requests.
- Reading HTML responses.
- Parsing HTML with Beautiful Soup.
- Finding elements using CSS selectors.
- Automating repetitive browser actions.

The scraping concepts learned from this project are still useful and can be applied to websites that allow automated access.

---

## Installation

Clone this repository:

```bash
git clone git@github.com:Joshua-2333/search-pypi.git
```

Navigate into the project directory:

```bash
cd search-pypi
```

Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

---

## Running the Program

Run the script with a search term:

```bash
python searchpypi.py requests
```

Other examples:

```bash
python searchpypi.py django
```

```bash
python searchpypi.py flask
```

---

## Project Structure

```
search-pypi/
│
├── searchpypi.py
├── README.md
└── .gitignore
```

---

## Lessons Learned

This project helped practice:

- Python modules and imports.
- Working with command-line arguments.
- Making HTTP requests.
- Parsing HTML documents.
- Using CSS selectors with Beautiful Soup.
- Automating browser tasks.
- Understanding the challenges of real-world web scraping.

A major lesson from this project is that web scraping requires continuous maintenance because websites frequently update their HTML structure and add protections against automated requests.

---

## Future Improvements

Possible improvements for this project:

- Update the scraper to work with a website that allows automated access.
- Use browser automation tools such as Selenium or Playwright.
- Add better error handling.
- Allow users to choose how many results to open.
- Add support for multiple search engines or websites.
