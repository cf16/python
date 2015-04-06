import operator

# numbers
imiona = list(set(list(input().split())))
d = dict({k: int(0) for k in imiona})
order = list(input().split())

for name in order:
    d[name] += 1

sorted_d = sorted(d.items(), key=operator.itemgetter(1))

sorted_d.reverse()
print(sorted_d)
