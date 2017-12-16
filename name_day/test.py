from unittest import TestCase, main

from name_day import NameDay


class NameDayTest(TestCase):
    def test_get_message(self):
        app = NameDay()
        self.assertRegex(
            app.get_message(),
            'Сегодня именины празднуют .*?'
        )


if __name__ == '__main__':
    main()
