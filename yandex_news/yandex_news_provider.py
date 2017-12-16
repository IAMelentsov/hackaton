from hakaton import MessageProvider
import feedparser
from random import randint

class YandexNewsProvider(MessageProvider):
    def __init__(self, rubric):
        super(MessageProvider, self).__init__()
        self._url = 'https://news.yandex.ru/' + rubric + '.rss'

    def get_message(self):
        feed = feedparser.parse(self._url)
        news_number = randint(0, len(feed["items"][:3])-1)
        try:
            result = feed["items"][news_number]["title"] + \
			    ". " + feed["items"][news_number]["summary"]
        except:
            result = ""
        return result