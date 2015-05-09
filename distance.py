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

def distance_simple(vertices1,vertices2):
    # print path up to root vertex
    id1 = vertices1[0]
    id2 = vertices2[0]
    length1 = 0
    length2 = 0
    while 1:
        # count path1 and path2 until vertex in vertices1 is
        # found in path2, then return sum of lengths
        found = False
        for it1 in vertices1:
            for it2 in vertices2: 
                if it1 == it2:
                    # found common vertex
                    found = True
                    return length1 + length2
                length2 = length2 + 1
            length2 = 0
            length1 = length1 + 1
        if found == False:
            # not found, error
            raise ValueError("No common vertex found.\n")
    return -1

def distance_notsimple(vertices1,vertices2):
    # print path up to root vertex
    id1 = vertices1[0]
    id2 = vertices2[0]
    length1 = 0
    length2 = 0
    while 1:
        # count path1 and path2 until vertex in vertices1 is
        # found in path2, then return sum of lengths
        found = False
        for it1 in vertices1:
            for it2 in vertices2: 
                if it1 == it2:
                    # found common vertex
                    found = True
                    return pow(2,length1) + pow(2,length2) - 2
                length2 = length2 + 1
            length2 = 0
            length1 = length1 + 1
        if found == False:
            # not found, error
            raise ValueError("No common vertex found.\n")
    return -1

# data
vertices = list()

# read input
tree_in = eval(input())
query_in = eval(input())

# get vertices list
tree_create(tree_in,vertices)
res = list()
for i in range (0,len(query_in)):
    e = query_in[i]
    if(e[0] == "prosta"):
        res.append(distance_simple(path_to_root(e[1],vertices),path_to_root(e[2],vertices)))
    elif(e[0] == "potegowa"):
        res.append(distance_notsimple(path_to_root(e[1],vertices),path_to_root(e[2],vertices)))
    else:
        raise ValueError("No common vertex found.\n")
print(res)
