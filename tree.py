import operator
import math

class Vertex():
   prev = ""
   id = ""
   def __init__(self,prev,id):
       self.prev = prev
       self.id = id
   #def area(self):
   #    s = 0.5*(self.a+self.b+self.c)
   #    return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

def path_to_root(id,vertices_list):
    # print path up to root vertex
    path = list()
    path.append(id)
    while 1:
        # print(id)
        ## path.append(it.id)
        #if v.prev == "":
        #    break
        # find vertex with id.prev
        found = False
        for it in vertices_list:
            if it.id == id:
                # found, it is vertex with this id
                found = True
                break
        if found == False:
            # not found, id is root index
            #path.append(it.prev)
            break
        id = it.prev
        path.append(id)
    return path

def tree_create(vertices_list,out):
    # create vertices and insert into out list        
    for i in range (0,len(vertices_list)):
        out.append(Vertex(vertices_list[i][0],vertices_list[i][1]))

# data
vertices = list()

# read input
tree_in = eval(input())
query_in = eval(input())

# print
#print("tree_in: ")
#print(tree_in)
#print("query_in: ")
#print(query_in)
print("\n")
# get vertices list
tree_create(tree_in,vertices)
#print(vertices)
for id in query_in:
    print(path_to_root(id,vertices))

