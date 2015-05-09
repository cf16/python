import operator
import math
import datetime

class Book():
    def __init__(self,title,author,year,dt):
        self.title = title
        self.author = author
        self.year = year
        self.dt = dt
    def __str__(self):
        return '%s, %s' %(self.title,self.author)

class Lib():
    limit = 1
    books = list()
    items = list()

    def __init__(self,limit):
        self.limit = limit

    def avail(self,l):
       for i in range (0,len(l)):
           print((l[i][0].title,l[i][0].author,l[i][1]))

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

    def dateFilter(self,dt):
        # delete if older
        self.items = [x for x in self.items if x[0].dt > dt]
        # for i in range (0,len(self.items)):
        #    if self.items[i][0].dt <= dt:
        #         del self.items[i]
        # count
        lcount = list()
        for i in range (0,len(self.items)):
            found = False
            for j in range (0,len(lcount)):
                if self.items[i][0].title == lcount[j][0].title and self.items[i][0].author == lcount[j][0].author:
                    # duplicate
                    found = True
                    lcount[j] = (lcount[j][0],lcount[j][1]+1)
                    break
            if found == False:
                # insert with 1
                lcount.append((self.items[i][0],1))
        return lcount
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
    l.add((Book(tup[0],tup[1],tup[2],datetime.date(tup[3][0],tup[3][1],tup[3][2]))))
inp = eval(input())
dt = datetime.date(inp[0],inp[1],inp[2])
dellist = l.dateFilter(dt)
dellist.sort(key=lambda x: x[0].title, reverse=False)    
l.avail(dellist)
