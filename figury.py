import operator
import math

class Circle():
   r = 0.0
   def __init__(self,r):
       self.r = r
   def area(self):
      return math.pi*self.r*self.r
      #return 9

class Rectangle():
   a = 0
   b = 0
   def __init__(self,a,b):
       self.a = a
       self.b = b
   def area(self):
       return(self.a*self.b)


class Triangle():
   a = 0.0
   b = 0.0
   c = 0.0
   def __init__(self,a,b,c):
       self.a = a
       self.b = b
       self.c = c
   def area(self):
       s = 0.5*(self.a+self.b+self.c)
       return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

# number of docs
n = int(input())
     
# lines
lines = []
figures = []
     
for i in range (0,n):
    line = list(input().lower().split())
    l = len(line)
    if l < 2:
        figures.append(Circle(float(line[0])))
    elif l == 2:
        figures.append(Rectangle(float(line[0]),float(line[1])))
    elif l == 3:
        figures.append(Triangle(float(line[0]),float(line[1]),float(line[2])))
    
sum = 0
for i in range (0,n):
    sum = sum + figures[i].area()
    
print(round(sum,2))
