"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_nnumbers(self):
        """Test adding numbers togther"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_number(self):

        res = calc.subtract_number(10, 15)
        self.assertEqual(res, 5)
