"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Tests for the calc module."""

    def test_add_numbers(self):
        """Test adding two numbers together."""
        res = calc.add(10, 5)

        self.assertEqual(res, 15)

    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)    