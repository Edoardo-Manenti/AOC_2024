import timeit
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
from operator import mul
import re




def parse_input(input_file):
    robots = []
    problems = input_file.strip().split("\n")
    for p in problems:
        c = p.split(" ")
        (s,v) = (c[0],c[1])
        (x,y) = s[2:].split(",")
        (vx,vy) = v[2:].split(",")
        (x,y) = int(x),int(y)
        (vx,vy) = int(vx),int(vy)
        robots.append([(x,y),(vx,vy)])
    return robots

def simulate(robot, iterations, w, h):
    x,y = robot[0]
    vx, vy = robot[1]
    return ((x+iterations*vx)%w, (y+iterations*vy)%h)

def plot_iteration(robots, w, h, iteration):
    for i,r in enumerate(robots):
        robots[i][0] = simulate(r, iteration, w, h)
    r_x = [r[0][0] for r in robots]
    r_y = [r[0][1] for r in robots]
    plt.scatter(r_x, r_y)
    plt.title("Seconds elapsed: {}".format(iteration))
    plt.show()
    return

def calc_variances(robots, w, h, iterations, plot=False):
    variances = []
    for i in range(iterations):
        for i,r in enumerate(robots):
            robots[i][0] = simulate(r, 1, w, h)
        positions = [[r[0][0], r[0][1]] for r in robots]
        var = np.var(positions)
        variances.append(var)
    if plot:
        plt.scatter(range(iterations), variances)
        plt.title("Variances for number of seconds elapsed")
        plt.show()
    return variances

def part1(input_file, w, h):
    robots = parse_input(input_file)
    tot = [0 for _ in range(4)]
    for r in robots:
        (x,y) = simulate(r, 100, w, h)
        if x < w//2:
            if y < h//2:
                tot[0] += 1
            elif y > h//2:
                tot[1] += 1
        elif x > w//2:
            if y < h//2:
                tot[3] += 1
            elif y > h//2:
                tot[2] += 1

    return reduce(mul, tot)

def part2(input_file, w, h, iterations):
    robots = parse_input(input_file)
    
    variances = calc_variances(robots, w, h, iterations)
    
    #Low percentile to make sure to avoid false positives
    target = np.percentile(variances, 0.000001)

    for i,v in enumerate(variances):
        if v < target:
            solution = i+1
            break

    robots = parse_input(input_file)
    plot_iteration(robots, w, h, solution)
    return solution

def solution():
    input_file = open("input.txt", "r").read()
    print(part1(input_file, 101, 103))
    print(part2(input_file, 101, 103, 10000))
    
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
