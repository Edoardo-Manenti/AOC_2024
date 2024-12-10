import timeit

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def create_map(input_file):
    return [[int(y) for y in list(x)] for x in input_file.split('\n') if len(x)!=0]

def find_zeros(map):
    zeros = []
    for i,r in enumerate(map):
        for j,elem in enumerate(r):
            if elem == 0:
                zeros.append((i,j))
    return zeros

def rec(curr_pos, map, m, n, peaks):
    for dir in directions:
        next = [sum(x) for x in zip(curr_pos, dir)]
        if next[0] in range(m) and next[1] in range(n):
            if map[next[0]][next[1]] - map[curr_pos[0]][curr_pos[1]] == 1:
                if map[next[0]][next[1]] == 9:
                    peaks.add(tuple(next)) 
                rec(next, map, m, n, peaks)

def part1(input_file):
    map = create_map(input_file)
    m = len(map)
    n = len(map[0])
    zeros = find_zeros(map)
    solution = 0
    for z in zeros:
        peaks = set([])
        rec(z, map, m, n, peaks)
        solution += len(peaks)
    return solution

def rec_plus(prev_pos, curr_pos, map, m, n, peaks):
    for dir in directions:
        next = [sum(x) for x in zip(curr_pos, dir)]
        if next[0] in range(m) and next[1] in range(n) and next != prev_pos:
            #print(next)
            if map[next[0]][next[1]] - map[curr_pos[0]][curr_pos[1]] == 1:
                if map[next[0]][next[1]] == 9:
                    peaks.append(tuple(next)) 
                rec_plus(curr_pos, next, map, m, n, peaks)

def part2(input_file):
    map = create_map(input_file)
    m = len(map)
    n = len(map[0])
    zeros = find_zeros(map)
    solution = 0
    for z in zeros:
        dp = [[False]*n]*m
        peaks = []
        rec_plus((-1,-1),z, map, m, n, peaks)
        #print("zero: {} peaks: {}".format(z, peaks))
        solution += len(peaks)
    return solution

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
