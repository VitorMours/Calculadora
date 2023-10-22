import unittest
from components import Display


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display()

    def test_if_display_has_padding(self):
        self.assertIsInstance(self, self.display.padding, int, "O display não possui um padding para melhor visibilidade")


if __name__ == '__main__':
    unittest.main(verbosity=2)
