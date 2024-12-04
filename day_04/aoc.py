
def part1(input_file):
    input_mat = []
    for m in input_file.split():
        input_mat.append(list(m))
    solution = 0
    #Check horizontal matches
    for i,l in enumerate(input_mat):
        j = 0
        while j < len(l)-3:
            if l[j:j+4] == ['X','M','A','S'] or l[j:j+4] == ['S','A','M','X']:
                solution += 1
            j+=1
    #Check vertical matches
    for i in range(len(input_mat)-3):
        j = 0
        while(j < len(input_mat[i])):
            k = []
            k.append(input_mat[i][j])
            k.append(input_mat[i+1][j])
            k.append(input_mat[i+2][j])
            k.append(input_mat[i+3][j])
            if k == ['X','M','A','S'] or k == ['S','A','M','X']:
                solution += 1
            j+=1
    #Check diagonal matches to the right
    for i in range(len(input_mat)-3):
        for j in range(len(input_mat[i])-3):
            k = []
            k.append(input_mat[i][j])
            k.append(input_mat[i+1][j+1])
            k.append(input_mat[i+2][j+2])
            k.append(input_mat[i+3][j+3])
            if k == ['X','M','A','S'] or k == ['S','A','M','X']:
                solution += 1
    #Check diagonal matches to the left
    for i in range(len(input_mat)-3):
        for j in range(3, len(input_mat[i])):
            k = []
            k.append(input_mat[i][j])
            k.append(input_mat[i+1][j-1])
            k.append(input_mat[i+2][j-2])
            k.append(input_mat[i+3][j-3])
            if k == ['X','M','A','S'] or k == ['S','A','M','X']:
                solution += 1
    return solution

def part2(input_file):
    input_mat = []
    for m in input_file.split():
        input_mat.append(list(m))
    solution = 0
    match = [['M','A','S','M','S'], ['M','A','S','S','M'],['S','A','M','M','S'],['S','A','M','S','M']]
    for i in range(len(input_mat)-2):
        for j in range(len(input_mat[i])-2):
            k = []
            k.append(input_mat[i][j])
            k.append(input_mat[i+1][j+1])
            k.append(input_mat[i+2][j+2])
            k.append(input_mat[i][j+2])
            k.append(input_mat[i+2][j])
            if k in match:
                solution += 1
    return solution

def solution():
    input_file = open("input.txt", "r").read()
    print(part1(input_file))
    print(part2(input_file))
    
if __name__ == "__main__":
    solution()
