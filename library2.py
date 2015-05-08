import operator
import math
import string
import sys

class Book():
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return '%s, %s' %(self.title,self.author)

class LibUser():
    #books = list()
    def __init__(self,name):
        self.name = name
        self.books = list()
    def add(self,b):
        # add book to my store
        self.books.append(b)
    def del_books(self,i):
        del self.books[i]

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
            if self.books[i][0].title == b.title:
                 self.books[i] = (self.books[i][0],self.books[i][1] + 1)
                 #del self.books[i]
                 #self.books.append(tmp)
                 return True
        self.books.append((b,1))
        return True
    def borrow(self,u,b):
        #print("borrow!\n")
        # user u tries to borrow book b
        if(len(u.books)>3):
            # he wants too much
            return False
        for i in range (0,len(u.books)):
            if u.books[i].title == b.title:
                # 2nd one?! hey!
                #print("2nd time!\n")
                return False
        for i in range (0,len(self.books)):
            if self.books[i][0].title == b.title:
                # found the book
                u.add(b)
                self.books[i] = (self.books[i][0],self.books[i][1] - 1)
                if(self.books[i][1]==0):
                    del self.books[i]
                return True
        return False
    def book_return(self,u,b):
        for i in range (0,len(u.books)):
            if u.books[i].title == b.title:
                self.add(b)
                u.del_books(i)
                return True
        return False

# program

# number of books
n = int(input())
     
# lines
lines = []
figures = []
l = Lib(100)
res = list()
users = list()
     
for i in range (0,n):
    #line = list(input().lower().split())
    found = False
    tup = eval(input())
    err = False
    if tup[0].strip() == "dodaj":
        err = l.add(Book(tup[1],tup[2],2015))
        res.append(err)
    elif tup[0].strip() == "wypozycz":
        for i in range (0,len(users)):
            if users[i].name == tup[1].strip():
                err = l.borrow(users[i],Book(tup[2],"default",2015))
                res.append(err)
                found = True
                #print("wypozyczanie found:")
                #for j in range (0,len(users)):
                #    for k in range (0,len(users[j].books)):
                #        print(users[j].books[k].title)
                #    print("|");
                #    sys.stdout.flush()
                continue
        if(found == False):
            user = LibUser(tup[1].strip())
            users.append(user)
            err = l.borrow(user,Book(tup[2],"default",2015))
            res.append(err) 
            #print("wypozyczanie NOT found:")
            #for j in range (0,len(users)):
            #    for k in range (0,len(users[j].books)):
            #        print(users[j].books[k].title)
            #    print("|");
            #    sys.stdout.flush()
    elif tup[0].strip() == "oddaj":
        for i in range (0,len(users)):
            if users[i].name == tup[1].strip():
                res.append(l.book_return(users[i],Book(tup[2],"default",2015)))
                found = True
             #   print("oddawanie found:\n")
             #   for j in range (0,len(users)):
             #       for k in range (0,len(users[j].books)):
             #           print(users[j].books[k].title)
             #       print("|");
             #       sys.stdout.flush()
                continue
        if(found == False):
            #print("!!!!!!!!!!!!!!!!!")
            u = LibUser(tup[1].strip())
            users.append(u)
            err = l.book_return(u,Book(tup[2],"default",2015))
            res.append(err)
            #print("oddawanie NOT found:\n")
            #for j in range (0,len(users)):
            #    for k in range (0,len(users[j].books)):
            #        print(users[j].books[k].title)
            #    print("|");
            #    sys.stdout.flush()
#l.books.sort(key=lambda x: x[0].title, reverse=False)    
#l.avail()
for i in range (0,len(res)):
    print(res[i])
