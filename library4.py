import operator
import math
import string
import sys
import datetime

class Book():
    def __init__(self,title,author,year,dt):
        self.title = title
        self.author = author
        self.year = year
        self.dt = dt
    def __str__(self):
        return '%s, %s' %(self.title,self.author)

class LibUser():
    #books = list()
    def __init__(self,name):
        self.name = name
        self.books = list()
        self.account = 0
    def __str__(self):
        return '%s, %s' %(self.name,self.account)

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
        # user u tries to borrow book b
        if(len(u.books)>3):
            # he wants too much
            return False
        for i in range (0,len(u.books)):
            if u.books[i].title == b.title:
                # 2nd one?! hey!
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
                # charge if kept book too long
                if (b.dt - u.books[i].dt).days > 7:           
                    # charge user: 0.5 PLN for each in excess of 7
                    for j in range (0,len(users)):
                        if users[j].name == u.name:
                            users[j].account = users[j].account + 0.5 * ((b.dt - u.books[i].dt).days - 7)
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
        dt = datetime.date(tup[4][0],tup[4][1],tup[4][2])
        err = l.add(Book(tup[1],tup[2],2015,dt))
        res.append(err)
    elif tup[0].strip() == "wypozycz":
        dt = datetime.date(tup[3][0],tup[3][1],tup[3][2])
        for i in range (0,len(users)):
            if users[i].name == tup[1].strip():
                err = l.borrow(users[i],Book(tup[2],"default",2015,dt))
                res.append(err)
                found = True
                continue
        if(found == False):
            user = LibUser(tup[1].strip())
            users.append(user)
            err = l.borrow(user,Book(tup[2],"default",2015,dt))
            res.append(err) 
    elif tup[0].strip() == "oddaj":
        dt = datetime.date(tup[3][0],tup[3][1],tup[3][2])
        for i in range (0,len(users)):
            if users[i].name == tup[1].strip():
                res.append(l.book_return(users[i],Book(tup[2],"default",2015,dt)))
                found = True
                continue
        if(found == False):
            u = LibUser(tup[1].strip())
            users.append(u)
            err = l.book_return(u,Book(tup[2],"default",2015,dt))
            res.append(err)

# charge as of today
today_in = eval(input())
today = datetime.date(today_in[0], today_in[1], today_in[2])
for k in range(0,len(users)):
    for i in range (0,len(users[k].books)):
            # charge if kept book too long
            if (today - users[k].books[i].dt).days > 7:           
                    # charge user: 0.5 PLN for each in excess of 7
                    users[k].account = users[k].account + 0.5 * ((today - users[k].books[i].dt).days - 7)

for i in range (0,len(res)):
    print(res[i])
users_res = list()
for j in range (0,len(users)):
    if users[j].account > 0:
        # print(users[j])
        tup = (users[j].name, users[j].account)
        # print(tup)
        users_res.append(tup)
users_res.sort(key = lambda tup: tup[0])
for i in range(0,len(users_res)):
    print(users_res[i])
