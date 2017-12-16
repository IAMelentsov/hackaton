from unittest import TestCase, main

from nameday import NamedayProvider


class NameDayTest(TestCase):
    def test_get_message(self):
        app = NamedayProvider()
        self.assertRegex(
            app.get_message(),
            'Сегодня именины празднуют .*?'
        )


if __name__ == '__main__':
    main()
