from hakaton import MessageProvider
import requests


class QuotationProvider(MessageProvider):
    _url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __init__(self, valutes=('USD', 'EUR')):
        super(MessageProvider, self).__init__()
        self._valutes = valutes

    def get_valute(self):
        valute = requests.get(self._url).json()['Valute']
        return [(valute[name]['Name'], valute[name]['Value']) for name in self._valutes]

    def get_message(self):
        return 'Курсы валют: %s' % ', '.join(
            map(lambda x: '%s – %s' % (x[0], x[1]), self.get_valute())
        )
