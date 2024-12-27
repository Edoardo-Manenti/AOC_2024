from collections import defaultdict
import heapq
import timeit

dir = [[0,1],[1,0],[0,-1],[-1,0]]

def find_start_end(input_file):
    maze = [list(r) for r in input_file.split("\n") if len(r) > 0]
    for i,h in enumerate(maze):
        for j,v in enumerate(h):
            if v == 'S':
                s = [i,j]
            elif v == 'E':
                e = [i,j]
    return s, e

def parse_input(input_file):
    maze = [[c != '#' for c in list(r)] for r in input_file.split("\n") if len(r) > 0]
    s, e = find_start_end(input_file)
    print("Start: {}\nEnd: {}".format(s,e))
    return maze, s, e

def get_neigh(maze, pos):
    neighbours = []
    for d in dir:
        next = [sum(x) for x in zip(pos, d)]
        x,y = next
        if next == pos:
            continue
        if x in range(len(maze)) and y in range(len(maze[0])):
            if maze[x][y]:
                neighbours.append((next, d))
    return neighbours

def get_neigh_cost(maze, pos, curr_dir):
    neighbours = []
    for d in dir:
        next = [sum(x) for x in zip(pos, d)]
        x,y = next
        if next == pos:
            continue
        if x in range(len(maze)) and y in range(len(maze[0])):
            if maze[x][y]:
                if d == curr_dir:
                    neighbours.append((next, d, 1))
                else:
                    neighbours.append((next, d, 1001))
    return neighbours

def rec(maze, curr, e, visited, cost, curr_dir, solutions):
    if cost > solutions:
        return solutions
    #print(cost)
    #print(curr)
    if curr == e:
        #print("Found END")
        if cost < solutions:
            solutions = cost
        return solutions
    visited[tuple(curr)]=cost
    #print(solutions)
    for n,d in get_neigh(maze, curr):
        if tuple(n) in visited.keys():
            if visited[tuple(n)]<cost:
                continue
        if d == curr_dir:
            solutions = rec(maze, n, e, visited, cost+1, d, solutions)
        else:
            solutions = rec(maze, n, e, visited, cost+1001, d, solutions)
    return solutions

def dijkstra(maze, s, e):
    sx, sy = s
    dx, dy = dir[0]
    pq = heapq.heapify([(0, sx, sy, dx, dy)])
    seen = [(sx, sy, dx, dy)]
    while pq:
        cost, cx, cy, dx, dy = heapq.heappop()
        if (cx, cy) == e:
            return cost
        seen.append((cx, cy, dx, dy))
        for next, d in get_neigh(maze, (dx, dy)):

def part1(input_file):
    maze, s, e = parse_input(input_file)
    visited = defaultdict(int)
    solutions = rec(maze, s, e, visited, 0, [0,1], 10000000)
    #print(visited)
    print(solutions)
    return solutions

def part2(input_file):
    maze, s, e = parse_input(input_file)
    visited = defaultdict(int)
    solution, path = rec2(maze, s, e, visited, 0, [0,1], 10000000, [])
    print(path)
    return solution

def solution():
    sys.setrecursionlimit(5000)
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
