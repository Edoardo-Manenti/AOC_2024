import unittest
from aoc import part1, part2, parse_input

class AocTestClass(unittest.TestCase):
    def test_parse_input(self):
        test_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
        value = parse_input(test_input)

    def test_part1(self):
        test_input = """#####
###E#
#...#
#.#.#
#...#
#.###
#S..#
#####
"""
        value = part1(test_input)
        exp_value = 3007
        self.assertEqual(value, exp_value)

    def test_part1_1(self):
        test_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
        value = part1(test_input)
        exp_value = 11048
        self.assertEqual(value, exp_value)

    def test_part2(self):
        test_input = """#####
###E#
#...#
#.#.#
#...#
#.###
#S..#
#####
"""
        value = part2(test_input)
        exp_value = 3007
        self.assertEqual(value, exp_value)

if __name__ == "__main__":
    unittest.main(verbosity=3)
