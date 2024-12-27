import re

reg = {}

def parse_input(input):
    s1, s2 = input.split("\n\n")
    registers = re.findall(reg_re, s1)
    program = list(re.findall(r"(\d)", s2))
    for k,v in registers:
        reg[k] = int(v)
    print(reg)
    print(program)
    return reg, program

def part1(input_file):
    l, ul, disp = parse_input(input_file)
    return 0

def part2():
    return 0

if __name__ == "__main__":
    input_file = open("input.txt", "r").read()
    print(part1(input_file))
    print(part2())