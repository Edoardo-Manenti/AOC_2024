import timeit
from collections import defaultdict

orth = [[0,1],[1,0],[0,-1],[-1,0]]

def find_regions(garden):
    regions = defaultdict(list)
    for i,r in enumerate(garden):
        for j,c in enumerate(r):
            plot = garden[i][j]
            if len(regions[plot])==0:
                regions[plot] = [[(i,j)]]
            else:
                appended = False
                for r in regions[plot]:
                    if appended:
                        break
                    for p in r:
                        if [sum(x) for x in zip(p,(-i,-j))] in orth:
                            r.append((i,j))
                            appended = True
                            break
                if not appended:
                    regions[plot].append([(i,j)])
    return regions

def find_perimeter(region):
    perimeter = 0
    for p in region:
        for o in orth:
            if tuple([sum(x) for x in zip(p, o)]) not in region:
                perimeter += 1
    return perimeter


def part1(input_file):
    garden = [list(x) for x in input_file.strip("\n\n").split("\n")]
    regions = find_regions(garden)
    solution = 0
    for r,v in regions.items():
        for i in v:
            per = find_perimeter(i)
            print("{} {}".format(r, per))
            solution += len(i)*per
    return solution

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
