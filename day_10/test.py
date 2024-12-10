import unittest
from aoc import part1, part2, create_map, rec, rec_plus

class AocTestClass(unittest.TestCase):
    def test_create_map(self):
        test_input = """0123
1234
8765
9876
"""
        value = create_map(test_input)
        expected_value = [[0,1,2,3],[1,2,3,4],[8,7,6,5],[9,8,7,6]]
        self.assertEqual(value, expected_value)

    def test_rec(self):
        test_input = """0123
1234
8765
9876
"""
        map = create_map(test_input)
        peaks = set([])
        dp = [[False]*4]*4
        rec((0,0), map, 4, 4, peaks)
        self.assertEqual(len(peaks), 1)

    def test_rec2(self):
        test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
        map = create_map(test_input)
        peaks = set([])
        rec((0,2), map, 8, 8, peaks)
        self.assertEqual(len(peaks), 5)

    def test_rec_plus(self):
        test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
        map = create_map(test_input)
        peaks = []
        rec_plus((-1,-1), (0,2), map, 8, 8, peaks)
        self.assertEqual(len(peaks), 20)

    def test_part1(self):
        test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
        value = part1(test_input)
        expected_value = 36
        self.assertEqual(value, expected_value)

    def test_part2(self):
        test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
        value = part2(test_input)
        expected_value = 81
        self.assertEqual(value, expected_value)


if __name__ == "__main__":
    unittest.main(verbosity=3)
