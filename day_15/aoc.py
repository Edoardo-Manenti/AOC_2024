import timeit

_dir = {'>':[0,1],'v':[1,0],'^':[-1,0],'<':[0,-1]}

def print_hall(hall):
    for r in hall:
            print(''.join(r))

def parse_input(input_file):
    h,m = input_file.split("\n\n")
    hall = [list(r) for r in h.split("\n") if len(r) > 0]
    moves = [_dir[d] for d in list(m.strip()) if d != '\n']
    #print(hall)
    #print(moves)
    return hall, moves

def find_robot(hall):
    for i,h in enumerate(hall):
        for j,v in enumerate(h):
            if v == '@':
                hall[i][j] = '.'
                return i,j

def gps(hall):
    gps = 0
    for i,x in enumerate(hall):
        for j,y in enumerate(x):
            if y in ['O','[']:
                gps += 100*i+j
    return gps

def stretch_hall(hall):
    result = []
    for i,r in enumerate(hall):
        result.append([])
        for j,c in enumerate(r):
            if c == '.':
                result[i].append('.')
                result[i].append('.')
            elif c == '#':
                result[i].append('#')
                result[i].append('#')
            elif c == '@':
                result[i].append('@')
                result[i].append('.')
            elif c == 'O':
                result[i].append('[')
                result[i].append(']')
    return result

def try_move(pos, d, hall, c):
    #print(pos)
    x,y = pos
    # I know there is a box in pos
    new_pos = [sum(x) for x in zip(pos, d)]
    x1,y1 = new_pos
    if hall[x1][y1] == '#':
        return False
    if hall[x1][y1] == '.':
        hall[x1][y1] = 'O'
        hall[x][y] = c
        return True
    if try_move(new_pos, d, hall, c):
        hall[x1][y1] = 'O'
        hall[x][y] = c
        return True
                
def part1(input_file):
    hall, moves = parse_input(input_file)
    rob = find_robot(hall)    
    w,h = len(hall), len(hall[0])
    for m in moves:
        #print("robot: {},{}".format(rob[0], rob[1]))
        pos = [sum(x) for x in zip(rob,m)]
        x,y = pos
        if hall[x][y] == '.':
            rob = pos
        elif hall[x][y] == '#':
            pass
        elif hall[x][y] == 'O':
            if try_move(pos, m, hall, '.'):
                rob = pos
    #print_hall(hall)
    return gps(hall) 

def can_move_thicc(pos, d, hall):
    #print(pos)
    x,y = pos
    # I know there is a box in pos
    new_pos = [sum(x) for x in zip(pos, d)]
    x1,y1 = new_pos
    if hall[x1][y1] == '#':
        return False
    if hall[x1][y1] == '.':
        return True
    if hall[x1][y1] == '[':
        if d == _dir['<']:
            if can_move_thicc((x1,y-1), d, hall):
                return True
            else:
                return False
        if d == _dir['>']:
            if can_move_thicc((x1,y1+1), d, hall):
                return True
            else:
                return False
        elif can_move_thicc(new_pos, d, hall) and can_move_thicc((x1,y1+1), d, hall):
            return True
        else:
            return False
    if hall[x1][y1] == ']':
        if d == _dir['>']:
            if can_move_thicc((x1,y+1), d, hall):
                return True
            else:
                return False
        if d == _dir['<']:
            if can_move_thicc((x1,y1-1), d, hall):
                return True
            else:
                return False
        elif can_move_thicc(new_pos, d, hall) and can_move_thicc((x1,y1-1), d, hall):
            return True
        else:
            return False

def try_move_thicc(pos, d, hall, c):
    #print(pos)
    x,y = pos
    # I know there is a box in pos
    new_pos = [sum(x) for x in zip(pos, d)]
    x1,y1 = new_pos
    if hall[x1][y1] == '#':
        return False
    if hall[x1][y1] == '.':
        hall[x1][y1] = hall[x][y]
        hall[x][y] = c
        return True
    if hall[x1][y1] == '[':
        if d == _dir['<']:
            if try_move_thicc((x1,y-1), d, hall, hall[x1][y1]):
                hall[x1][y1] = hall[x][y]
                hall[x][y] = c
                return True
            else:
                return False
        if d == _dir['>']:
            if try_move_thicc((x1,y1+1), d, hall, hall[x1][y1]):
                hall[x1][y1] = hall[x][y]
                hall[x][y] = c
                return True
            else:
                return False
        elif can_move_thicc(new_pos, d, hall) and can_move_thicc((x1,y1+1), d, hall):
            try_move_thicc(new_pos, d, hall, hall[x][y]) 
            try_move_thicc((x1,y1+1), d, hall, '.')
            hall[x][y] = c
            return True
        else:
            return False
    if hall[x1][y1] == ']':
        if d == _dir['>']:
            if try_move_thicc((x1,y+1), d, hall, hall[x1][y1]):
                hall[x1][y1] = hall[x][y]
                hall[x][y] = c
                return True
            else:
                return False
        if d == _dir['<']:
            if try_move_thicc((x1,y1-1), d, hall, hall[x1][y1]):
                hall[x1][y1] = hall[x][y]
                hall[x][y] = c
                return True
            else:
                return False
        elif can_move_thicc(new_pos, d, hall) and can_move_thicc((x1,y1-1), d, hall):
            try_move_thicc(new_pos, d, hall, hall[x][y])
            try_move_thicc((x1,y1-1), d, hall, '.')
            hall[x][y] = c
            return True
        else:
            return False

def part2(input_file):
    hall, moves = parse_input(input_file)
    hall = stretch_hall(hall)
    rob = find_robot(hall)    
    w,h = len(hall), len(hall[0])
    print("\nStarting hall:")
    print("robot: {},{}".format(rob[0], rob[1]))
    print_hall(hall)
    for m in moves:
        #print(m)
        r1,r2 = rob
        pos = [sum(x) for x in zip(rob,m)]
        x,y = pos
        if hall[x][y] == '.':
            rob = pos
        elif hall[x][y] == '#':
            pass
        elif hall[x][y] == '[':
            if m == _dir['>']:
                rob = pos if try_move_thicc(pos, m, hall, '.') else rob
            elif can_move_thicc(pos, m, hall) and can_move_thicc((x,y+1), m, hall):
                try_move_thicc(pos, m, hall, '.')
                try_move_thicc((x,y+1), m, hall, '.')
                rob = pos
        elif hall[x][y] == ']':
            if m == _dir['<']:
                rob = pos if try_move_thicc(pos, m, hall, '.') else rob
            elif can_move_thicc(pos, m, hall) and can_move_thicc((x,y-1), m, hall):
                try_move_thicc(pos, m, hall, '.')
                try_move_thicc((x,y-1), m, hall, '.')
                rob = pos
        #print("robot after move: {},{}".format(rob[0], rob[1]))
    print("\nFinisched hall:")
    print("robot: {},{}".format(rob[0], rob[1]))
    print_hall(hall)
    return gps(hall) 

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
