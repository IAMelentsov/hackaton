from datetime import datetime
from urllib.request import urlopen
from re import findall, search, sub

from hakaton import MessageProvider


class NameDay(MessageProvider):
    def __init__(self):
        super(MessageProvider, self).__init__()
        self._url = 'http://www.calend.ru/names/%d-%d/'

    @staticmethod
    def _request(url):
        response = urlopen(url)

        return response.read().decode('windows-1251')

    @staticmethod
    def _parse(html):
        return findall(
            '<ahref="/names/0/0/\d+/">(.*?)</a>',
            search(
                '<li><strong>Именины</strong>(.*?)</li>',
                sub('[\s\t]', '', html)
            ).group(1)
        )

    def get_message(self):
        now = datetime.now()

        return "Сегодня именины празднуют %s" % ', '.join(
            self._parse(
                self._request(
                    self._url % (now.month, now.day)
                )
            )
        )
