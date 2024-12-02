import time


def main():
    aoc1()

def aoc1():
    f = open("input_aoc1.txt", "r")
    l1, l2 = parse_input(f.read())
    #print(l1[:10])
    #print(l2[:10])
    res1 = solution1(l1, l2)
    res2 = solution2(l1, l2)
    print(res1)
    print(res2)

def parse_input(input_string):
    l1, l2 = [], []
    for i, n in enumerate(input_string.split()):
       if(i%2 == 0): 
        l1.append(int(n))
       else:
        l2.append(int(n))
    return l1, l2

def solution1(l1, l2):
    res = 0
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        res += abs(l1[i]-l2[i])
    return res

def solution2(l1, l2):
    res = 0
    l2.sort()
    for i in range(len(l1)):
        to_find = l1[i]
        counter, j = 0, 0
        while(j < len(l2) and l2[j]<=to_find):
            if(l2[j] == to_find): counter = counter+1
            j = j+1
        res += to_find*counter
    return res

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
