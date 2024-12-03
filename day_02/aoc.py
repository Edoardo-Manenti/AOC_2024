import time


def main():
    aoc1()

def aoc1():
    f = open("input.txt", "r")
    l1 = parse_input(f.read())
    #l1 = parse_input("1 2 7 8 9")
    #print(l1[:10])
    res1 = solution1(l1)
    res2 = solution2(l1)
    print(res1)
    print(res2)

def parse_input(input_string):
    l1 = input_string.split("\n")
    d1 = []
    for i,l in enumerate(l1):
        d1.append([int(item) for item in l.split()])
    return d1

def solution1(l1):
    res = sum(check_list(l) for l in l1)
    return res

def solution2(l1):
    res = 0
    for l in l1:
        if(check_list(l)!=1):
            print(l)
            for i in range(len(l)):
                l2 = [e for j,e in enumerate(l) if j != i]
                print(l2)
                if check_list(l2) == 1:
                    res+=1
                    break
        else:
            res+=1
    return res

def check_list(l):
    i = 0
    inc = True
    if len(l) == 0:
        return False
    if len(l) == 1:
        return True
    while(i<len(l)-1):
        if inc:
            if l[i]>=l[i+1]:
                if i==0 and l[i]!=l[i+1]:
                    inc = False
                else:
                    break
        else:
            if l[i]<=l[i+1]:
                    break
        if abs(l[i+1]-l[i])>3:
            break
        i+=1
    if i==len(l)-1: 
        return 1
    else:
        return 0

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
