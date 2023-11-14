class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item): #push
        self.items.append(item)

    def pop(self): #pop
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self): #return element at the head
        return self.items[len(self.items)-1]
    
# Node class
class node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as None

# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, node = None):
        if node is None: #head
            node = self.head
            
        print(node.data)
        if node.next is None: #tail
            return node
        else:
            self.traverse(node.next)


    def insertAtHead(self,d):
        newNode = node(d)
        if(self.head):
            newNode.next = self.head
        else:
            self.head = newNode
          
    def insertAtTail(self,d):
        newNode = node(d)
        if(self.head):
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode
        else:
            self.head = newNode


    def deleteAtHead(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None

    def size(self):
        if(self.head):
            s = 1
            temp = self.head
            while(temp):
                s+=1
                temp = temp.next
            return s
        return 0
    
    def top(self):
        return self.head
    
class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def add_child(self, child):
        self.children.append(child)

    def traverse(self):
        print(self.data) # 1 2 5 3 4
        if len(self.children) == 0: 
            return
        else:
            for child in self.children: #t -> [c1, c2, c3] c1 -> [c4]
                child.traverse()
                        
    def DFS(self):
        explore = Stack()
        visited = []
        explore.push(self)
        while(explore.size()):
            a = explore.top()
            visited.append(a.data)
            explore.pop()
            for child in a.children :
                explore.push(child)
        return visited
    
    def BFS(self):
        explore = LinkedList()
        visited = []
        explore.insertAtTail(self)
        while(explore.size()):
            a = explore.head.data
            visited.append(a.data)
            explore.deleteAtHead()
            for child in a.children :
                explore.insertAtTail(child)
        return visited
      

c1 = Tree(2)
c2 = Tree(7)
c3 = Tree(5)
c4 = Tree(12)
c5 = Tree(10)
c6 = Tree(6)
c7 = Tree(9)
c8 = Tree(11)
c9 = Tree(4)

c1.add_child(c2)
c1.add_child(c3)
c2.add_child(c4)
c2.add_child(c5)
c2.add_child(c6)
c3.add_child(c7)
c7.add_child(c9)
c6.add_child(c8)

print(c1.DFS())
print(c1.BFS())
