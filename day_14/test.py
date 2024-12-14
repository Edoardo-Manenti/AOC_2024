import unittest
from aoc import part1, part2, parse_input, simulate

class AocTestClass(unittest.TestCase):
    def test_parse_input(self):
        test_input = """p=0,4 v=3,-3
"""
        value = parse_input(test_input)
        exp_value = [[(0,4),(3,-3)]]

        self.assertEqual(value, exp_value)

    def test_simulate(self):
        r = [(0,0), (2,1)]
        iterations = 3
        
        value = simulate(r, iterations, 5, 5)
        exp_value = (1,3)

        self.assertEqual(value, exp_value)


    def test_part1(self):
        test_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
        value = part1(test_input, 11, 7)
        exp_value = 12

        self.assertEqual(value, exp_value)

    def test_part2(self):
        test_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""
        value = part2(test_input, 11, 7, 100)

if __name__ == "__main__":
    unittest.main(verbosity=3)
