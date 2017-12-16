from unittest import TestCase, main

from nameday import NamedayProvider


class NamedayProviderTest(TestCase):
    def setUp(self):
        self.app = NamedayProvider(16, 12)

    def test_get_names(self):
        self.assertEqual(
            self.app.get_names(),
            ['Андрей', 'Гавриил', 'Георгий', 'Ефрем', 'Иван', 'Николай', 'Федор']
        )

    def test_get_message(self):
        self.assertRegex(
            self.app.get_message(),
            'Сегодня именины празднуют Андрей, Гавриил, Георгий, Ефрем, Иван, Николай, Федор'
        )


if __name__ == '__main__':
    main()
