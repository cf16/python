import operator

# number of docs
n = int(input())

# lines
lines = []

for i in range (0,n):
    line = list(input().lower().split())
    lines.append(line)

# number of queries
m = int(input())
query = [None] * m

for i in range (0,m):
    query[i] = input().lower()

for i in range(0,m):
    arr = [[0 for x in range(2)] for x in range(n)]
    d = dict({k: int(0) for k in range(n)})
    for h in range(0,n):
        arr[h][0] = h
        arr[h][1] =  int(lines[h].count(query[i]))
        d[h] = int(lines[h].count(query[i]))
    #print(arr)
    d = {key: value for key, value in d.items() if value is not 0}
    d1 = sorted(d.items(), key=lambda x: (x[1],x[0]), reverse=True)
    #reverse_comparison = lambda (a1, a2),(b1, b2):cmp((b2, a1), (a2, b1))
    d4 = sorted(d.items(), key=lambda x: (-x[1],x[0]))
    #print(d1)
    #d1.reverse()
    #print(d4)
    l5 = []
    for x in d4:
        l5.append(x[0])
    print(l5)
    #d2 = dict(d1)
    #d3 = sorted(d2.items(), key=operator.itemgetter(0))
    #print("d3:\n")
    #print(d3)
    #print(d.items())
#imiona = list((input().split())
#d = dict({k: int(0) for k in imiona})
#order = list(input().split())

#for name in order:
#    d[name] += 1

#sorted_d = sorted(d.items(), key=operator.itemgetter(1))

#sorted_d.reverse()
#print(sorted_d)
