
l = []

def fibo(n):
    if n < 0:
        return -1
    if n == 0:
        #l += [0]
        return 0
    if n == 1:
        #l += [1]
        return 1
    if n == 2:
        #l += [2]
        return 1

    #l += [n]
    return fibo( n-1) + fibo( n-2)

# number
n_ = int(input())

fibo(n_)
i = 0 
while i < n_: 
  l +=  [fibo(i)]
  i = i + 1

print(l)
