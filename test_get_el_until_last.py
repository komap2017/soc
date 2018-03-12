from unittest import TestCase
from soc import get_el_until_last

class TestGet_el_until_last(TestCase):
    def test_get_el_until_last(self):
        self.assertEqual(['1', '2', '3'], get_el_until_last(['1', '2', '3'], '4'))
        self.assertEqual(['1', 2], get_el_until_last(['1', 2, '3'], 2))
        self.assertEqual([], get_el_until_last([], 'random'))