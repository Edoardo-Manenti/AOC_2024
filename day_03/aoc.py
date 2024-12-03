import re

def part1(input_file):
    regex1 = r'mul\((\d*),(\d*)\)'
    list1 = re.findall(regex1, input_file)
    solution1 = sum([int(v1)*int(v2) for v1,v2 in list1])
    return solution1

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
    print(part1(input_file))
    print(part2(input_file))
    
if __name__ == "__main__":
    solution()