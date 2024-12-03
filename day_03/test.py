import unittest
from aoc import part1, part2

class AocTestClass(unittest.TestCase):
    def test_part1(self):
        test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        value = part1(test_input)
        expected_value = 161
        self.assertEqual(value, expected_value)

    def test_part2(self):
        test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        value = part2(test_input)
        expected_value = 48
        self.assertEqual(value, expected_value)

if __name__ == "__main__":
    unittest.main(verbosity=2)