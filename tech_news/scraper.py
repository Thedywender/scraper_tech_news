import requests
import time
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except (requests.exceptions.RequestException, requests.Timeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    list_of_links = []
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        links = [link.get("href") for link in soup.select("h2.entry-title a")]
        list_of_links.extend(links)
        return list_of_links
    except ValueError:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError