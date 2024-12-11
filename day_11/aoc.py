import timeit
from collections import defaultdict


def blink(stones):
    i = 0
    length = len(stones)
    while i in range(length):
        s = stones[i]
        if s==0:
            stones[i]=1
        elif len(str(s))%2==0:
            l = len(str(s))
            old, new = int(str(str(s)[:l//2])), int(str(str(s)[l//2:]))
            stones[i]=old
            stones.append(new)
        else:
            stones[i]=stones[i]*2024
        i+=1

def blink_but_faster(stone_dict):
    stone_cp = dict(stone_dict)

    for stone, count in stone_cp.items():
        if count==0: continue
        if stone==0:
            stone_dict[0]-=count
            stone_dict[1]+=count
        elif len(str(stone))%2==0:
            l = len(str(stone))
            old, new = int(str(str(stone)[:l//2])), int(str(str(stone)[l//2:]))
            stone_dict[old]+=count
            stone_dict[new]+=count
            stone_dict[stone]-=count
        else:
            stone_dict[stone]-=count
            stone_dict[stone*2024]+=count
    return


def part1(input_file, num_blinks=25):
    stones = [int(x) for x in input_file.split(" ")]
    for i in range(num_blinks):
        blink(stones)
    return len(stones)

def part2(input_file, num_blinks=75):
    stones = [int(x) for x in input_file.split(" ")]
    stone_dic = defaultdict(int)
    for s in stones:
        stone_dic[s]+=1
    for i in range(num_blinks):
        blink_but_faster(stone_dic)
    return sum(stone_dic.values())

def solution():
    input_file = open("input.txt", "r").read().strip("\n")
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
