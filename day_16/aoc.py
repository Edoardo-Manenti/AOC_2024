import timeit

dir = [[0,1],[1,0],[0,-1],[-1,0]]

def print_maze(hall):
    for r in hall:
            print(''.join(r))

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
    print(maze)
    print("Start: {}\nEnd: {}".format(s,e))
    return maze, s, e

def get_neigh(maze, pos):
    neighbours = []
    for d in dir:
        next = [sum(x) for x in zip(pos, d)]
        x,y = next
        if x in range(len(maze)) and y in range(len(maze[0])):
            if maze[x][y]:
                neighbours.append(next)
    return neighbours

def backtrack(maze, s, e, solution):
    result = [e]
    last_idx = solution.index(e)
    last = e
    while last != s:
        for n in get_neigh(maze, last):
            if n in solution:
                i = solution.index(n)
                if i < last_idx:
                    result.append(n)
                    last = n
                    last_idx = i
    result.reverse()
    return result
                
def calc_cost(solution):
    cost = 0
    for i,r in enumerate(solution):
        if i == 0:
            last_pos = r
            last_dir = dir[0]
        x,y = r
        x1,y1 = last_pos
        d = [x-x1, y-y1]
        if d == last_dir:
            cost += 1
        elif d == dir[(dir.index(last_dir)+2)%4]:
            cost += 2001
        else:
            cost += 1001
        last_dir = d
        last_pos = r
    return cost

def bfs(maze, s, e):
    solution = []
    frontier = []
    visited = []

    frontier.append(s)
    visited.append(s)

    while frontier:
        next = frontier.pop(0)
        if next == e:
            solution.append(next)
            break
        solution.append(next)
        for neigh in get_neigh(maze, next):
            if neigh not in visited:
                frontier.append(neigh)
                visited.append(neigh)

    print(solution)
    solution = backtrack(maze, s, e, solution)
    return solution

def part1(input_file):
    maze, s, e = parse_input(input_file)
    solution = bfs(maze, s, e)
    print(solution)
    cost = calc_cost(solution)
    print(cost)
    return 0

def part2(input_file):
    return 0

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
