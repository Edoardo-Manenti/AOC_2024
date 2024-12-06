import timeit

def create_room(input_file):
    return [list(i) for i in input_file.split("\n") if len(list(i)) != 0]

def find(element, matrix):
    for i, matrix_i in enumerate(matrix):
        for j, value_j in enumerate(matrix_i):
            if value_j == element:
                return i,j
    return None

def part1(input_file):
    room = create_room(input_file)
    i,j = find('^', room)
    solution = set([(i,j)])
    room[i][j] = '.'
    directions = [[-1,0], [0, 1], [1,0], [0, -1]]
    curr_dir = directions[0]
    while(i+curr_dir[0]<len(room) and j+curr_dir[1]<len(room[0])):
        if room[i+curr_dir[0]][j+curr_dir[1]]=='.':
            i += curr_dir[0]
            j += curr_dir[1]
        else:
            next_dir_idx = (directions.index(curr_dir)+1)%len(directions)
            curr_dir = directions[next_dir_idx]
            i += curr_dir[0]
            j += curr_dir[1]
        solution.add((i,j))
    return solution

def is_loop(room):
    i,j = find('^', room)
    corners = set()
    last_corner = None
    directions = [[-1,0], [0, 1], [1,0], [0, -1]]
    curr_dir = directions[0]
    while(i+curr_dir[0]<len(room) and j+curr_dir[1]<len(room[0])
          and i+curr_dir[0]>=0 and j+curr_dir[1]>=0):
        if room[i+curr_dir[0]][j+curr_dir[1]]!='#':
            i += curr_dir[0]
            j += curr_dir[1]
        else:
            next_dir_idx = (directions.index(curr_dir)+1)%len(directions)
            curr_dir = directions[next_dir_idx]
            if (i,j) in corners and (i,j) != last_corner: return True 
            else: 
                corners.add((i,j))
                last_corner = (i,j)
        
    return False

def part2(input_file):
    room = create_room(input_file)
    solution = 0
    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] not in ['#', '^']:
                room[i][j] = '#'
                if is_loop(room): 
                    solution += 1
                room[i][j] = '.'
    return solution

def part2_but_faster(input_file):
    room = create_room(input_file)
    solution = 0
    beaten_path = part1(input_file)
    for p in beaten_path:
        i = p[0]
        j = p[1]
        if room[i][j] not in ['#', '^']:
            room[i][j] = '#'
            if is_loop(room): 
                solution += 1
            room[i][j] = '.'

    return solution

def solution():
    input_file = open("input.txt", "r").read()
    #print(len(part1(input_file)))
    #print(part2(input_file))
    #print(part2_but_faster(input_file))
    
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
