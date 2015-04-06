
def factorial(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial( n-1)

# numbers
lst = list(map(int, input().split()))
n = lst[0];
m = lst[1];

# last digit
n_ = int(n)
m_ = int(m)

print(int( factorial(n_) / ( factorial(m_) * factorial(n_ - m_))))
