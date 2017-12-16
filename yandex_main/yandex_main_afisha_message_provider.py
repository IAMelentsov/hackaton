from yandex_main import YandexMainMessageProvider

class YandexMainAfishaMessageProvider(YandexMainMessageProvider):
    def __init__(self, *args, **keyArgs):
        super(YandexMainAfishaMessageProvider, self).__init__()

    def get_message(self):
        soup = self.get_soup()
        afisha = soup.find('div', { "class": "afisha" })
        items = afisha.find_all('a', { "class": "b-afisha__item" })
        films_list = list(map(self.get_title_from_item, items))

        return "Сегодня в кино: " + ", ".join(films_list)

    def get_title_from_item(self, item):
        if "title" in item.attrs:
            return item.attrs["title"]
        return item.getText()

if __name__ == '__main__':
    ymmp = YandexMainAfishaMessageProvider()
    print(ymmp.get_message())
