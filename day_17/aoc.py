import re

reg = {}

def parse_input(input):
    reg_re = r"Register (A|B|C): (\d*)"
    s1, s2 = input.split("\n\n")
    registers = re.findall(reg_re, s1)
    program = list(re.findall(r"(\d)", s2))
    for k,v in registers:
        reg[k] = int(v)
    print(reg)
    print(program)
    return reg, program

def combo(operand):
    if operand in ('0', '1', '2', '3'):
        return int(operand)
    elif operand == '4':
        return reg["A"]
    elif operand == '5':
        return reg["B"]
    elif operand == '6':
        return reg["C"]

def operate(currop, opcode, operand, output):
    #print(reg)
    #print(currop, opcode, operand, output)
    if opcode == '0':
        reg['A'] = reg["A"]//(2**(combo(operand)))
    elif opcode == '1':
        reg['B'] = reg['B'] ^ int(operand)
    elif opcode == '2':
        reg['B'] = combo(operand)%8
    elif opcode == '3':
        if reg['A'] != 0:
            return int(operand)
    elif opcode == '4':
        reg['B'] = reg['B'] ^ reg['C']
    elif opcode == '5':
        output.append(str(combo(operand)%8))
    elif opcode == '6':
        reg['B'] = reg["A"]//(2**(combo(operand)))
    elif opcode == '7':
        reg['C'] = reg["A"]//(2**(combo(operand)))
    return currop + 2

def part1(operations):
    i = 0
    output = []
    while i < len(operations) and i+1 < len(operations):
        i = operate(i, operations[i], operations[i+1], output)
    #print(reg)
    return output

def is_close(output, operations, level):
    if len(output) != len(operations):
        return False
    count = 0
    for i,o in enumerate(output):
        if o == operations[i]:
            count += 1
        else:
            break
    count >= level

def program(input):
    #print("{:b}".format(input))
    output = []
    a = input
    b = c = 0
    while a != 0:
        b = a % 8
        b = b ^ 5
        c = a // (2**b)
        b = b ^ 6
        a = a // 8
        b = b ^ c
        output.append(str(b%8))
    return output

def part2():
    curr = 8**16
    output = program(curr)
    while output != operations and curr > 8**15:
        curr -= 1
        output = program(curr)
        if is_close(output, operations, 6):
            print(curr)
    return curr

if __name__ == "__main__":
    input_file = open("input.txt", "r").read()
    memory, operations = parse_input(input_file)
    print(','.join(part1(operations)))
    print(part2())