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
