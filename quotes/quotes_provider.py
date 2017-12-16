from urllib.request import HTTPSHandler, build_opener, install_opener
import json
import ssl

from hakaton import MessageProvider


class QuotesProvider(MessageProvider):
    def __init__(self, valutes=('USD', 'EUR')):
        super(MessageProvider, self).__init__()
        self._valutes = valutes

    @staticmethod
    def _request():
        https_sslv3_handler = HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
        opener = build_opener(https_sslv3_handler)
        install_opener(opener)
        response = opener.open('https://www.cbr-xml-daily.ru/daily_json.js')

        return response.read().decode('utf-8')

    def get_valute(self):
        valute = json.loads(self._request())['Valute']
        return [(name, valute[name]['Value']) for name in self._valutes]

    def get_message(self):
        return 'Курсы валют: %s' % ', '.join(
            map(lambda x: '%s – %s' % (x[0], x[1]), self.get_valute())
        )
