def program(input):
    print("{:b}".format(input))
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
    print(','.join(output))
    print("end")

program((1<<45))
program((1<<45) + 1)
program((1<<45) + (1<<3))
program((1<<45) + (1<<3) + (1<<4))
program((1<<45) + (1<<3) + (1<<4) + 1)
#program((1<<45) + (1<<3) + 1)

