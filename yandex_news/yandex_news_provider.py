from random import randint
from hakaton import MessageProvider
import feedparser
import requests


class YandexNewsProvider(MessageProvider):
    def __init__(self, rubric):
        super(MessageProvider, self).__init__()
        self._url = 'https://news.yandex.ru/' + rubric + '.rss'

    def get_message(self):
        feed = feedparser.parse(requests.get(self._url).content)
        news_number = randint(0, len(feed["items"][:3]) - 1)
        result = ""
        try:
            result = feed["items"][news_number]["title"] + \
                     ". " + feed["items"][news_number]["summary"]
        finally:
            return result
