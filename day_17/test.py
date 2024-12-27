import unittest
from aoc import parse_input, part1

class AocTestClass(unittest.TestCase):
    def test_parse_input(self):
        test_input = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""
        parse_input(test_input)

    def test_part1(self):
        test_input = """
Register A: 0
Register B: 29
Register C: 0

Program: 1,7
"""
        memory, operations = parse_input(test_input)
        print(part1(operations))

    def test_part2(self):
        test_input = """
Register A: 117440
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
        memory, operations = parse_input(test_input)
        print(part1(operations))

if __name__ == "__main__":
    unittest.main(verbosity=3)