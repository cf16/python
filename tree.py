import operator
import math

class Vertex():
   prev = ""
   id = ""
   def __init__(self,id,prev):
       self.prev = prev
       self.id = id
   #def area(self):
   #    s = 0.5*(self.a+self.b+self.c)
   #    return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

def path_to_root(v):
    # print path up to root vertex
    path = list()
    while 1:
        # print(id)
        path.append(v.id)
        if v.prev == "":
            break
        # find vertex with id.prev
        found = False
        for v in vertices_list:
            if v.id == id.prev:
                # found
                found = True
                break
        if found == False:
            raise ValueError('path_to_root: Index not found!')

def tree_create(vertices_list,out):
    # create vertices and insert into out list        
    for i in range (0,len(vertices_list)):
        out.append(vertices_list[i])

# data
vertices = list()

# read input
tree_in = eval(input())
query_in = eval(input())

# print
print("tree_in: ")
print(tree_in)
print("query_in: ")
print(query_in)
print("\n")
# get vertices list
tree_create(tree_in,vertices)
print(vertices)
for v in query_in:
    

