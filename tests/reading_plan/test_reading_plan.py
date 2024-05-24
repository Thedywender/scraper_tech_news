from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService
import pytest

news_data = [
    {"title": "Python", "reading_time": 4},
    {"title": "Pytest", "reading_time": 3},
    {"title": "Parsel", "reading_time": 10},
    {"title": "Beautiful Soup", "reading_time": 15},
    {"title": "Requests", "reading_time": 20},
]

expected_results = {
    "readable": [
        {"unfilled_time": 8, "chosen_news": [("Python", 4), ("Pytest", 3)]},
        {"unfilled_time": 5, "chosen_news": [("Parsel", 10)]},
        {"unfilled_time": 0, "chosen_news": [("Beautiful Soup", 15)]},
    ],
    "unreadable": [("Requests", 20)],
}


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = lambda: news_data

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    result = ReadingPlanService.group_news_for_available_time(15)
    assert result == expected_results
