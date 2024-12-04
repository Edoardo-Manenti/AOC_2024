import re

def part1(input_file):
    input_mat = []
    for m in input_file.split():
        input_mat.append(list(m))
    solution = 0
    #Check horizontal matches
    for i,l in enumerate(input_mat):
        j = 0
        while j < len(l)-4:
            if l[j:j+4] == ['X','M','A','S'] or l[j:j+4] == ['S','A','M','X']:
                print("H: i={} j={}".format(i, j))
                solution += 1
            j+=1
    #Check vertical matches
    for i in range(len(input_mat)-4):
        j = 0
        while(j < len(input_mat[i])):
            if i >= len(input_mat)-4:
                break
            k = []
            k.append(input_mat[i][j])
            k.append(input_mat[i+1][j])
            k.append(input_mat[i+2][j])
            k.append(input_mat[i+3][j])
            if k == ['X','M','A','S'] or k == ['S','A','M','X']:
                print("V: i={} j={}".format(i, j))
                solution += 1
            j+=1
    #Check diagonal matches to the right
    for i in range(len(input_mat)-4):
        for j in range(len(input_mat[i])-4):
            k = []
            k.append(input_mat[i][j])
            k.append(input_mat[i+1][j+1])
            k.append(input_mat[i+2][j+2])
            k.append(input_mat[i+3][j+3])
            if k == ['X','M','A','S'] or k == ['S','A','M','X']:
                print("Dr: i={} j={}".format(i, j))
                solution += 1
    #Check diagonal matches to the left
    for i in range(3, len(input_mat)):
        for j in range(len(input_mat[i])-4):
            k = []
            k.append(input_mat[i][j])
            k.append(input_mat[i-1][j-1])
            k.append(input_mat[i-2][j-2])
            k.append(input_mat[i-3][j-3])
            if k == ['X','M','A','S'] or k == ['S','A','M','X']:
                print("Dl: i={} j={}".format(i, j))
                solution += 1
    return solution

def part2(input_file):
    regex2 = r'(don\'t\(\))|(do\(\))|mul\((\d*),(\d*)\)'
    list2 = re.findall(regex2, input_file)
    solution2 = 0
    enabled = True
    for e in list2:
        if(e[0] == "don't()"):
            enabled = False
        if(e[1] == "do()"):
            enabled = True
        if(enabled and e[2] != '' and e[3]!=''):
            solution2 += int(e[2])*int(e[3])
    return solution2

def solution():
    input_file = open("input.txt", "r").read()
    test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    print(part1(test_input))
    #print(part1(input_file))
    #print(part2(input_file))
    
if __name__ == "__main__":
    solution()