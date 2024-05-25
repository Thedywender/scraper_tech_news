from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news_return_data = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    news_data = [(new["title"], new["url"]) for new in news_return_data]
    return news_data


# Requisito 8
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

    news_return_data = db.news.find(
        {"timestamp": {"$regex": date, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    news_data = [(new["title"], new["url"]) for new in news_return_data]
    return news_data


# Requisito 9
def search_by_category(category):
    news_return_data = db.news.find(
        {"category": {"$regex": category, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )

    news_data = [(new["title"], new["url"]) for new in news_return_data]
    return news_data
