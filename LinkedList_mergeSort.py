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
            
    def insert(self, insert_node, after_node = None):
        if after_node is None: #insert at the start
            insert_node.next = self.head
            self.head = insert_node
            return 
        elif after_node.next is None: #insert at the end
            after_node.next = insert_node
            insert_node.next = None
        else: #insert in the middle
            insert_node.next = after_node.next
            after_node.next = insert_node

    def display(self,h):
        while(h):
            print(h.data , end = " ")
            h = h.next
        print()
    def findMid(self,h):
        tortoise = h
        hare = h
        while(hare.next and hare.next.next):
            hare = hare.next.next
            tortoise = tortoise.next
        return tortoise
    
    def mergeSort(self,h):
        if (h.next):
            left = h
            mid = self.findMid(left)
            right = mid.next
            mid.next = None
            # self.mergeSort(left)
            # self.mergeSort(right)
            return self.merge(self.mergeSort(left),self.mergeSort(right))
        else:
            return h
    
    def merge(self,l1,l2):
        n = node(None)
        ll = LinkedList()
        ll.head = n
        while((l1) and (l2)):
            if(l1.data <= l2.data):
                n1 = node(l1.data)
                n.next = n1
                n = n.next
                l1 = l1.next
            else :
                n2 = node(l2.data)
                n.next = n2
                n = n.next
                l2 = l2.next
        #print(l1,l2)	
        while(l1):
            n1 = node(l1.data)
            n.next = n1
            n = n.next
            l1 = l1.next
        while(l2):
            n2 = node(l2.data)
            n.next = n2
            n = n.next
            l2 = l2.next
        ll.head = ll.head.next
        return ll.head

def display(h):
        while(h):
            print(h.data , end = " ")
            h = h.next
        print()

l = LinkedList()
n1 = node(1)
n2 = node(69)
n3 = node(2)
n4 = node(-4)
n5 = node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
l.head = n1
display(l.head)
display(l.mergeSort(l.head))
