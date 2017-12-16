from unittest import TestCase, main

from quotes import QuotesProvider


class NameDayTest(TestCase):
    def test_get_valute(self):
        app = QuotesProvider(['EUR'])
        valute = app.get_valute()
        self.assertEqual(len(valute), 1)

    def test_get_message(self):
        app = QuotesProvider()
        self.assertRegex(
            app.get_message(),
            'Курсы валют: USD – \d\d.\d{4}, EUR – \d\d.\d{4}'
        )


if __name__ == '__main__':
    main()
