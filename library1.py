import operator
import math

class Book():
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return '%s, %s' %(self.title,self.author)

class Lib():
    limit = 1
    books = list()
    items = list()
    def __init__(self,limit):
        self.limit = limit
    def avail(self):
       for i in range (0,len(self.books)):
           print((self.books[i][0].title,self.books[i][0].author,self.books[i][1]))
       #return 9
    def add(self,b):
        # add item, always
        self.items.append((b,1))
        # add book if necessary
        for i in range (0,len(self.books)):
            if self.books[i][0].title == b.title and self.books[i][0].author == b.author:
                 self.books[i] = (self.books[i][0],self.books[i][1] + 1)
                 #del self.books[i]
                 #self.books.append(tmp)
                 return
        self.books.append((b,1))
        return

# program

# number of books
n = int(input())
     
# lines
lines = []
figures = []
l = Lib(100)
     
for i in range (0,n):
    #line = list(input().lower().split())
    tup = eval(input())
    #print(tup)
    l.add((Book(tup[0],tup[1],tup[2])))

l.books.sort(key=lambda x: x[0].title, reverse=False)    
l.avail()
