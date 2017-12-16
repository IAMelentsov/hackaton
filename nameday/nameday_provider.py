from datetime import datetime
from urllib.request import urlopen
from re import findall, search, sub

from hakaton import MessageProvider


class NamedayProvider(MessageProvider):
    _url = 'http://www.calend.ru/names/%d-%d/'

    def __init__(self, day=datetime.now().day, month=datetime.now().month):
        super(MessageProvider, self).__init__()
        self._day = day
        self._month = month

    @staticmethod
    def _request(url):
        response = urlopen(url)

        return response.read().decode('windows-1251')

    def get_names(self):
        return findall(
            '<aclass="\w+"href="/names/0/0/\d+/">(.*?)</a>',
            search(
                '<divclass="holidayweek">(.*?)</div><divclass="mm2">',
                sub('[\s\t\n\r]', '', self._request(self._url % (self._month, self._day)))
            ).group(1)
        )

    def get_message(self):
        return "Сегодня именины празднуют %s" % ', '.join(self.get_names())
