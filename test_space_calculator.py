"""
Name: Roseann Lawson
Course: CIS105 - Introduction to Python Programming
Assignment: Exercise Assignment 4
Description: Unit Tests for Space Mission Calculator
"""

import unittest

from space_calculator import (
    miles_to_kilometers,
    calculate_travel_time,
    calculate_fuel_needed,
    check_fuel_supply
)


class TestSpaceCalculator(unittest.TestCase):

    def test_miles_to_kilometers(self):
        self.assertAlmostEqual(
            miles_to_kilometers(100),
            160.934,
            places=3
        )

    def test_calculate_travel_time(self):
        self.assertEqual(
            calculate_travel_time(1000, 250),
            4
        )

    def test_calculate_fuel_needed(self):
        self.assertEqual(
            calculate_fuel_needed(1000, 0.5),
            500
        )

    def test_check_fuel_supply_true(self):
        self.assertTrue(
            check_fuel_supply(500, 600)
        )

    def test_check_fuel_supply_false(self):
        self.assertFalse(
            check_fuel_supply(500, 400)
        )


if __name__ == "__main__":
    unittest.main()
