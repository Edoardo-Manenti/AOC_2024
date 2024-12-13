import timeit
import math
import re
from collections import defaultdict

def parse_input(input_file):
    regex = r"Button A: X\+(\d*), Y\+(\d*)\nButton B: X\+(\d*), Y\+(\d*)\nPrize: X=(\d*), Y=(\d*)\n*"
    values = re.findall(regex, input_file)
    return values

def solve(p, solutions):
    (a1, a2, b1, b2, p1, p2) = (int(p[0]), int(p[1]), int(p[2]), int(p[3]), int(p[4]), int(p[5]))
    A = (p2*b1 - b2*p1)/(a2*b1-a1*b2)
    B = (p1-a1*A)/b1
    A2 = int(A)
    B2 = int(B)

    if abs(A2-A)>0.01:
        return
    if abs(B2-B)>0.01:
        return
    cost = 3*A + B
    solutions.append(cost)
    return cost

def solve2(p, solutions):
    (a1, a2, b1, b2, p1, p2) = (int(p[0]), int(p[1]), int(p[2]), int(p[3]), int(p[4]), int(p[5]))
    p1 = 10000000000000 + p1
    p2 = 10000000000000 + p2
    A = (p2*b1 - b2*p1)/(a2*b1-a1*b2)
    B = (p1-a1*A)/b1
    A2 = int(A)
    B2 = int(B)

    if abs(A2-A)>0.01:
        return
    if abs(B2-B)>0.01:
        return
    #if A2 + B2 > 100:
    #    return
    cost = 3*A + B
    solutions.append(cost)
    return cost

def part1(input_file):
    problems = parse_input(input_file)
    print(problems)
    solutions = []
    for p in problems:
        solve(p, solutions)
    return sum(solutions)

def part2(input_file):
    problems = parse_input(input_file)
    print(problems)
    solutions = []
    for p in problems:
        solve2(p, solutions)
    return sum(solutions)

def solution():
    input_file = open("input.txt", "r").read()
    print(part1(input_file))
    print(part2(input_file))
    
def performance():
    my_setup = '''
from aoc import part1, part2
input_file = open("input.txt", "r").read()
'''
    print("Time for part1: {} sec".format(timeit.timeit(setup=my_setup, stmt='part1(input_file)', number = 1)))
    print("Time for part2: {} sec".format(timeit.timeit(setup=my_setup, stmt='part2(input_file)', number = 1)))

if __name__ == "__main__":
    solution()
    #performance()
