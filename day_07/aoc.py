import timeit
import re
import math

def parse_input(input_file: str):
    rows = [x.split(": ") for x in input_file.split("\n") if len(x)!=0]
    target = [int(r[0]) for r in rows]
    numbers = [[int(n) for n in r[1].split()] for r in rows]
    return target, numbers

def rec(target, current, numbers, length, with_concat=False):
    if len(numbers) == 1:
        result = set([])
        result.add(current+numbers[0])
        result.add(current*numbers[0])
        if with_concat:
            result.add(int(str(numbers[0]) + str(current)))
        return result
    else:
        result = rec(target, numbers[0], numbers[1:], length, with_concat)
        new_result = set([])
        for r in list(result):
            new_result.add(current+r)
            new_result.add(current*r)
            if with_concat:
                new_result.add(int(str(r) + str(current)))
        return new_result

def brute_force(target, numbers, with_concat=False):
    numbers.reverse()
    possible_results = list(rec(target, numbers[0], numbers[1:], len(numbers), with_concat)) 
    if target not in list(possible_results):
        return 0
    return target

def part1(input_file):
    target, numbers = parse_input(input_file)
    return sum([brute_force(t, numbers[i]) for i, t in enumerate(target)])
    

def part2(input_file):
    target, numbers = parse_input(input_file)
    return sum([brute_force(t, numbers[i], True) for i, t in enumerate(target)])

def solution():
    input_file = open("input.txt", "r").read()
    print(part1(input_file))
    print(part2(input_file))
    
def performance():
    my_setup = '''
from aoc import part1, part2, part2_but_faster
input_file = open("input.txt", "r").read()
'''
    print("Time for part1: {} sec".format(timeit.timeit(setup=my_setup, stmt='part1(input_file)', number = 1)))
    print("Time for part2: {} sec".format(timeit.timeit(setup=my_setup, stmt='part2(input_file)', number = 1)))
    print("Time for part2_bit_faster: {} sec".format(timeit.timeit(setup=my_setup, stmt='part2_but_faster(input_file)', number = 1)))

if __name__ == "__main__":
    solution()
    #performance()
