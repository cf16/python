# count occurences of words that begins from uppercase letter

#licznik
count = 0
array = []

for i in range(0,5):
    array.append( input())

for i in range(0,5):
    s = array[i]
    if s[0] == s[0].upper():
        count = count + 1

# result
print(count)


