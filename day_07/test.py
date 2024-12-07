import unittest
from aoc import part1, part2, brute_force

class AocTestClass(unittest.TestCase):
    def test_brute_force1(self):
        value = brute_force(5, [1,2,3])
        expected_value = 5
        self.assertEqual(value, expected_value)

    def test_brute_force2(self):
        value = brute_force(7290, [6,8,6,15])
        expected_value = 0
        self.assertEqual(value, expected_value)

    def test_part1(self):
        test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
        value = part1(test_input)
        expected_value = 3749
        self.assertEqual(value, expected_value)


    def test_part2(self):
        test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
        value = part2(test_input)
        expected_value = 11387
        self.assertEqual(value, expected_value)

if __name__ == "__main__":
    unittest.main(verbosity=3)
