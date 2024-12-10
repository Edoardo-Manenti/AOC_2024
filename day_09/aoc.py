import timeit

def create_memory(input_file: str):
    memory = []
    i=0
    to_append = ''
    while i in range(len(input_file)):
        if i%2 == 0:
            to_append = str(i//2)
        else:
            to_append = '.'
        for j in range(int(input_file[i])):
                memory.append(to_append)
        i+=1
    return memory

def checksum(memory: list):
    result=0
    for i,m in enumerate(memory):
        if m == '.':
            continue
        result += i*int(m)
    return result

def part1(input_file):
    memory = create_memory(input_file)
    l=0
    r=len(memory)-1
    while l<r:
        if memory[l]!= '.':
            l+=1
            continue
        if memory[r] == '.':
            r-=1
            continue
        memory[l] = memory[r]
        memory[r] = '.'
        l+=1
        r-=1
    return checksum(memory)

def chunk_length(memory, start, ascending=True):
    length = 1
    curr_chunk = memory[start]
    dir = 1 if ascending else -1
    start+=1*dir
    while start in range(len(memory)):
        if memory[start]!=curr_chunk:
            break
        length+=1
        start+=1*dir
    return length


def reorder_page(memory):
    l=0
    r=len(memory)-1
    while l<r:
        if memory[l]!= '.':
            l+=1
            continue
        if memory[r] == '.':
            r-=1
            continue
        while l<r:
            if memory[l]!= '.':
                l+=1
                continue
            size_free = chunk_length(memory, l)
            size_page = chunk_length(memory, r, False)
            if size_free >= size_page:
                for i in range(size_page):
                    memory[l] = memory[r]
                    memory[r] = '.'
                    l+=1
                    r-=1
                break
            l+=size_free
        r=r if l<r else r-size_page
        l=0
    return memory


def part2(input_file):
    memory = create_memory(input_file)
    return checksum(reorder_page(memory))

def solution():
    memory = open("input.txt", "r").read().strip('\n')
    print(part1(memory))
    print(part2(memory))
    
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
