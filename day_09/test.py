import unittest
from aoc import part1, part2, create_memory, chunk_length

class AocTestClass(unittest.TestCase):
    def test_create_memory(self):
        test_input = """12345"""
        value = create_memory(test_input)
        expected_value = ['0','.','.','1','1','1','.','.','.','.','2','2','2','2','2']
        self.assertEqual(value, expected_value)
        
    def test_create_memory_0(self):
        test_memory = ['0','.','.','1','1','1','.','.','.','.','2','2','2','2','2']
        value = chunk_length(test_memory, 0)
        expected_value = 1
        self.assertEqual(value, expected_value)

    def test_create_memory_1(self):
        test_memory = ['0','.','.','1','1','1','.','.','.','.','2','2','2','2','2']
        value = chunk_length(test_memory, 1)
        expected_value = 2
        self.assertEqual(value, expected_value)

    def test_create_memory_2(self):
        test_memory = ['0','.','.','1','1','1','.','.','.','.','2','2','2','2','2']
        value = chunk_length(test_memory, len(test_memory)-1, False)
        expected_value = 5
        self.assertEqual(value, expected_value)

    def test_part1(self):
        test_input = """2333133121414131402"""
        value = part1(test_input)
        expected_value = 1928
        self.assertEqual(value, expected_value)

    def test_part2(self):
        test_input = """2333133121414131402"""
        value = part2(test_input)
        expected_value = 2858
        self.assertEqual(value, expected_value)

if __name__ == "__main__":
    unittest.main(verbosity=3)
