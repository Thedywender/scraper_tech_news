import requests
import time
import re
from bs4 import BeautifulSoup
from tech_news.database import create_news


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
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        url = soup.find("link", rel="canonical")["href"]
        title = soup.find(class_="entry-title").get_text(strip=True)
        timestamp = soup.find(class_="meta-date").get_text()
        writer = soup.find(class_="author").find("a").text
        reading_time_text = soup.find(class_="meta-reading-time").text
        reading_time = int(re.search(r"\d+", reading_time_text).group())
        summary = (
            soup.select_one("div.entry-content p")
            .text.replace("n/", "")
            .strip()
        )
        category = soup.find(class_="label").text

        news_dict = {
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "reading_time": reading_time,
            "summary": summary,
            "category": category,
        }
        return news_dict
    except Exception as e:
        print(f"Exception: {e}")
        return {}


# Requisito 5
def get_tech_news(amount):
    tech_news = []
    url = "https://blog.betrybe.com/"

    while len(tech_news) < amount:
        html_content = fetch(url)
        updates = scrape_updates(html_content)
        for link in updates:
            if len(tech_news) < amount:
                news_html = fetch(link)
                news = scrape_news(news_html)
                tech_news.append(news)
        next_page_link = scrape_next_page_link(html_content)
        if next_page_link:
            url = next_page_link
        else:
            break
    create_news(tech_news)
    return tech_news
