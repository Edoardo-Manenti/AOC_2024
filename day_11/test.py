import unittest
from aoc import part1, part2, blink

class AocTestClass(unittest.TestCase):
    def test_part1_1(self):
        test_input = """125 17"""
        value = part1(test_input, 6)
        expected_value = 22
        self.assertEqual(value, expected_value)
        
    def test_part1(self):
        test_input = """125 17"""
        value = part1(test_input)
        expected_value = 55312
        self.assertEqual(value, expected_value)

    def test_part2(self):
        test_input = """125 17"""
        value = part2(test_input, 25)
        expected_value = 55312
        self.assertEqual(value, expected_value)
if __name__ == "__main__":
    unittest.main(verbosity=3)
