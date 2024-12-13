import unittest
from aoc import part1, part2, parse_input, solve

class AocTestClass(unittest.TestCase):
    def test_parse_input(self):
        test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
        value = parse_input(test_input)

    def test_solve(self):
        test_input = (94, 34, 22, 67, 8400, 5400)

        value = solve(test_input, [])
        exp_value = 280

        self.assertEqual(value, exp_value)

    def test_part1(self):
        test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
        value = part1(test_input)
        exp_value = 480

        self.assertEqual(value, exp_value)

        
    def test_part2(self):
        test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
        value = part2(test_input)
        exp_value = 0

        self.assertEqual(value, exp_value)
if __name__ == "__main__":
    unittest.main(verbosity=3)
