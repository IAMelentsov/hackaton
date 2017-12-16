from unittest import TestCase, main

from nameday import NamedayProvider


class NameDayTest(TestCase):
    def setUp(self):
        self.app = NamedayProvider(16, 12)

    def test_get_names(self):
        self.assertEqual(
            self.app.get_names(),
            ['Андрей', 'Гавриил', 'Георгий', 'Иван', 'Николай', 'Федор', 'Ефрем']
        )

    def test_get_message(self):
        self.assertRegex(
            self.app.get_message(),
            'Сегодня именины празднуют Андрей, Гавриил, Георгий, Иван, Николай, Федор, Ефрем'
        )


if __name__ == '__main__':
    main()
