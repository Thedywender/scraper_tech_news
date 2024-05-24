from tech_news.database import db


# Requisito 7
def search_by_title(title):
    news_return_data = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    return [(new["title"], new["url"]) for new in news_return_data]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
