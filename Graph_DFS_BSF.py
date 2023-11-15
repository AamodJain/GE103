def edgeListToDict(edgeList):  # edgeList = [('a','b'),('a','c'),('a','d'),('b','c'),('b','e'),('b','d'),('c','e'),('c','d')] -->
                               # degeDict = {'a': ['b', 'c', 'd'], 'b': ['a', 'c', 'e', 'd'], 'c': ['a', 'b', 'e', 'd'], 'd': ['a', 'b', 'c'], 'e': ['b', 'c']}
    d = {}
    for i in edgeList:
        d[i[0]]=[]
        d[i[1]]=[]
    for i in edgeList:
        d[i[0]].append(i[1])
        d[i[1]].append(i[0])
    return d

def BSF(d,starting_node):
    #global d
    visited_nodes = []
    explore = []
    explore.append(starting_node)
    while(len(explore)):
        current_node = explore.pop(0)
        visited_nodes.append(current_node)
        for neighbour in d[current_node]:
            if ((neighbour not in visited_nodes) and (neighbour not in explore)) :
                explore.append(neighbour)
    return visited_nodes

def DSF(d,starting_node):
    visited_nodes = []
    explore = []
    explore.append(starting_node)
    while(len(explore)):
        current_node = explore.pop(0)
        visited_nodes.append(current_node)
        for neighbour in d[current_node]:
            if ((neighbour not in visited_nodes) and (neighbour not in explore)) :
                explore.insert(0,neighbour)
    return visited_nodes

def DSF_2(d,starting_node):
    visited_nodes = []
    explore = []
    explore.append(starting_node)
    while(len(explore)):
        current_node = explore.pop(0)
        if(current_node not in visited_nodes):
            visited_nodes.append(current_node)
            for neighbour in d[current_node]:
                if ((neighbour not in visited_nodes)) :
                    explore.insert(0,neighbour)
    return visited_nodes

d = {'a':['b','e'],'b':['a','c','d'],'c':['b','d'],'d':['b','c','e'],'e':['a','d']}
sn = input()
#print("BSF --> ",BSF(d,sn))
print("DSF --> ",DSF_2(d,sn))
