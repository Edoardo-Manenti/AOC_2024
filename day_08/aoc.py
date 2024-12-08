import timeit

def parse_input(input_file: str):
    rows = [x for x in input_file.split("\n") if len(x)!=0]
    _map = [list(x) for x in rows]
    antennas = {}
    for i in range(len(_map)):
        for j in range(len(_map[i])):
            if _map[i][j] != '.':
                curr_freq = _map[i][j]
                if curr_freq not in antennas.keys():
                    antennas[curr_freq] = [(i, j)]
                else:
                    antennas[curr_freq].append((i, j))
    return antennas, len(rows[0]), len(rows)

def find_antinodes(a1, a2):
    r1, c1 = a1[0], a1[1]
    r2, c2 = a2[0], a2[1]

    v = (r2-r1, c2-c1)
    _v = tuple([-x for x in list(v)])

    n1 = tuple([sum(x) for x in zip(a1, _v)])
    n2 = tuple([sum(x) for x in zip(a2, v)])

    return [n1, n2]

def check_antinode(cols,rows, antinode):
    if antinode[0] in range(rows) and antinode[1] in range(cols):
       return True
    else:
       return False

def part1(input_file):
    antennas, cols, rows = parse_input(input_file)
    antinodes = []
    for freq in antennas.keys():
        locations = antennas[freq]
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                antinodes += find_antinodes(locations[i], locations[j])

    return sum([1 for a in set(antinodes) if check_antinode(cols, rows, a)])
    
def find_antinodes_plus(cols, rows, a1, a2):
    antinodes = [a1, a2]
    r1, c1 = a1[0], a1[1]
    r2, c2 = a2[0], a2[1]

    v = (r2-r1, c2-c1)
    _v = tuple([-x for x in list(v)])

    n1 = tuple([sum(x) for x in zip(a1, _v)])
    n2 = tuple([sum(x) for x in zip(a2, v)])

    while(check_antinode(cols, rows, n1)):
        antinodes.append(n1)
        n1 = tuple([sum(x) for x in zip(n1, _v)])

    while(check_antinode(cols, rows, n2)):
        antinodes.append(n2)
        n2 = tuple([sum(x) for x in zip(n2, v)])

    return antinodes

def part2(input_file):
    antennas, cols, rows = parse_input(input_file)
    antinodes = []
    for freq in antennas.keys():
        locations = antennas[freq]
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                antinodes += find_antinodes_plus(cols, rows, locations[i], locations[j])

    return len(set(antinodes))

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
    performance()
