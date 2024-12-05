import unittest
from aoc import part1, part2

class AocTestClass(unittest.TestCase):
    def test_part1(self):
        test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
        value = part1(test_input)
        expected_value = 143
        self.assertEqual(value, expected_value)


    def test_part2(self):
        test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
        value = part2(test_input)
        expected_value = 123
        self.assertEqual(value, expected_value)
if __name__ == "__main__":
    unittest.main(verbosity=3)
