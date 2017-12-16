from unittest import TestCase, main

from quotation import QuotationProvider


class QuotationProviderTest(TestCase):
    def test_get_valute(self):
        app = QuotationProvider(['EUR'])
        valute = app.get_valute()
        self.assertEqual(len(valute), 1)

    def test_get_message(self):
        app = QuotationProvider()
        self.assertRegex(
            app.get_message(),
            'Курсы валют: Доллар США – \d\d.\d{4}, Евро – \d\d.\d{4}'
        )


if __name__ == '__main__':
    main()
