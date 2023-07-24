"""
Sample tests
"""
from django.test import SimpleTestCase

from . import calc


class CalculatorTests(SimpleTestCase):
    """ Test the calc module """
    def test_add_numbers(self):
        """ Test adding two numbers """
        res = calc.add(3, 6)
        self.assertEqual(res, 9)

    def test_subtract_numbers(self):
        """ Testing subtracting two numbers """
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)
