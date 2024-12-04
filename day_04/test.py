import unittest
from aoc import part1, part2

class AocTestClass(unittest.TestCase):
    def test_part1(self):
        test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        value = part1(test_input)
        expected_value = 18
        self.assertEqual(value, expected_value)

    def test_part2(self):
        test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
        value = part2(test_input)
        expected_value = 9
        self.assertEqual(value, expected_value)
if __name__ == "__main__":
    unittest.main(verbosity=2)
