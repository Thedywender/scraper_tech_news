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
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        next_page = soup.select_one("a.next.page-numbers")
        if next_page:
            return next_page.get("href")
        return None
    except ValueError:
        return None


# Requisito 4
def scrape_news(html_content):
    #     {
    #   "url": "https://blog.betrybe.com/novidades/noticia-bacana",
    #   "title": "Notícia bacana",
    #   "timestamp": "04/04/2021",
    #   "writer": "Eu",
    #   "reading_time": 4,
    #   "summary": "Algo muito bacana aconteceu",
    #   "category": "Ferramentas",
    # }
    news_dict = dict()
    try:
        soup = BeautifulSoup(html_content, "html.parser")

        news_dict["url"] = soup.find("h2.entry-title").text
        news_dict["title"] = soup.find("h1.entry-title a").text
        news_dict["timestamp"] = soup.find("li.meta-date").text
        news_dict["writer"] = soup.find("span.fn a").text
        news_dict["reading_time"] = int(soup.find("li.cs-icon").text)
        news_dict["summary"] = soup.select_one("div.entry-content p em").text
        news_dict["category"] = soup.find("span.label").text
        return news_dict
    except ValueError:
        return {}


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
