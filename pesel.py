# validates the pessel number

# pesel
p = input();

# last digit
d = int(p) % 10

# hipothetical digit
h = int(p[0]) + int(p[1])*3 + int(p[2])*7 + int(p[3])*9 + int(p[4]) + int(p[5])*3 + int(p[6])*7 + int(p[7])*9 + int(p[8]) + int(p[9])*3

# test
if d == 10 - h % 10:
    print(1)
else:
    print(0)
