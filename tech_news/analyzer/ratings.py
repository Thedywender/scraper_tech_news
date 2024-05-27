from collections import Counter
from tech_news.database import db


def top_5_categories():
    news_data = db.news.find({}, {"category": 1, "_id": 0})
    categories = [new["category"] for new in news_data if "category" in new]
    category_counts = Counter(categories)
    most_common_categories = category_counts.most_common(5)
    most_common_categories.sort(key=lambda x: (-x[1], x[0]))

    return [category for category, count in most_common_categories]
