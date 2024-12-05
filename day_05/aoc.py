import re

def part1(input_file):
    regex_rules = r'(\d*)\|(\d*)'
    input_file = input_file.split("\n\n")
    input_rules, input_manuals = input_file[0], input_file[1]
    rules = re.findall(regex_rules, input_rules)
    manuals = [x.split(",") for x in input_manuals.split("\n")]

    solution = 0

    for m in manuals:
        relevant_rules = [r for r in rules if set(r).issubset(m)]
        counter = 0
        length = len(m)
        for i,n in enumerate(m):
            if not set([rule[1] for rule in relevant_rules if rule[0]==n]).issubset(m[i:]):
                break
            else:
                counter += 1
        if counter == length:
            print(m)
            print(m[length//2])
            solution += int(m[length//2]) 

    return solution

def part2(input_file):
    regex_rules = r'(\d*)\|(\d*)'
    input_file = input_file.split("\n\n")
    input_rules, input_manuals = input_file[0], input_file[1]
    rules = re.findall(regex_rules, input_rules)
    manuals = [x.split(",") for x in input_manuals.split("\n")]

    solution = 0

    for m in manuals:
        relevant_rules = [r for r in rules if set(r).issubset(m)]
        corrected = False
        length = len(m)
        print(m)
        i = 0
        while i<length:
            n = m[i]
            to_swap = set([rule[1] for rule in relevant_rules if rule[0]==n]).difference(m[i:])
            if not len(to_swap)==0:
                if not corrected:
                    corrected = True
                to_swap = list(to_swap)[0]
                print("swap {} and {}".format(to_swap, n))
                m[m.index(to_swap)] = n
                m[i] = to_swap
                i = 0
            else:
                i=i+1
        if corrected:
            print(m)
            print(m[length//2])
            solution += int(m[length//2]) 

    return solution

def solution():
    input_file = open("input.txt", "r").read()
    print(part1(input_file))
    print(part2(input_file))
    
if __name__ == "__main__":
    solution()
