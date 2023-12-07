import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import logging
from time import sleep

logging.basicConfig(level=logging.INFO)

def fetch_sitemap(url, session):
    response = session.get(url)
    response.raise_for_status()
    return response.text

def parse_sitemap(sitemap_content):
    root = ET.fromstring(sitemap_content)
    urls = [url.text for url in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    return urls

def crawl_url(url, session):
    response = session.get(url)
    return response.text

def save_data(filename, data):
    with open(filename, 'a') as file:
        file.write(data + "\n")

def main():
    sitemap_url = input("Enter the sitemap URL: ")
    session = requests.Session()
    session.headers.update({'User-Agent': 'Your Custom User Agent'})

    try:
        sitemap_content = fetch_sitemap(sitemap_url, session)
        urls = parse_sitemap(sitemap_content)

        for url in urls:
            try:
                page_content = crawl_url(url, session)
                # Optional: Process page_content with BeautifulSoup here
                save_data("overview.md", page_content)
                sleep(1)  # Rate limiting
            except Exception as e:
                logging.error(f"Error crawling {url}: {e}")

    except Exception as e:
        logging.error(f"Error fetching sitemap: {e}")

if __name__ == "__main__":
    main()
