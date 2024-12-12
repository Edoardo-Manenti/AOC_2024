import unittest
from aoc import part1, part2, find_regions

class AocTestClass(unittest.TestCase):
    def test_find_regiorns(self):
        test_input = """AAAA
BBCD
BBCC
EEEC
"""
        garden = [list(x) for x in test_input.strip("\n\n").split("\n")]
        regions = find_regions(garden)
        expected_value = {'A': [[(0, 0), (0, 1), (0, 2), (0, 3)]], 'B': [[(1, 0), (1, 1), (2, 0), (2, 1)]], 'C': [[(1, 2), (2, 2), (2, 3), (3, 3)]], 'D': [[(1, 3)]], 'E': [[(3, 0), (3, 1), (3, 2)]]}
        self.assertEqual(regions, expected_value)
        
    def test_part1_1(self):
        test_input = """AAAA
BBCD
BBCC
EEEC
"""
        value = part1(test_input)
        expected_value = 140
        self.assertEqual(value, expected_value)

    def test_part1_2(self):
        test_input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
        value = part1(test_input)
        expected_value = 1930
        self.assertEqual(value, expected_value)

    def test_part2(self):
        test_input = """125 17"""
        value = part2(test_input)
        expected_value = 55312
        self.assertEqual(value, expected_value)
if __name__ == "__main__":
    unittest.main(verbosity=3)
