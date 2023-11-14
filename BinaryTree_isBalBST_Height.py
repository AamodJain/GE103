class binaryTree:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def addRight(self,r):
        self.right = r
    def addLeft(self,l):
        self.left = l
    def height(self):
        if(self.left and self.right):
            return 1+max(self.left.height(),self.right.height())
        elif(self.right):
            return 1+(self.right.height())
        elif(self.left):
            return 1+(self.left.height())
        else :
            return 1
        
    def is_balanced_BST(self):
        if(self.left and self.right):
            if abs(self.left.height() - self.right.height())>1:
                return False
            else:
                return (self.left.is_balanced_BST() & self.right.is_balanced_BST())
        elif(self.left):
            if(self.left.height()>1):
                return False
        elif(self.right):
            if(self.right.height()>1):
                return False
        return True

            

        

t1 = binaryTree(1)
t2 = binaryTree(2)
t3 = binaryTree(3)
t4 = binaryTree(4)
t5 = binaryTree(5)
t6 = binaryTree(6)
t7 = binaryTree(7)

t1.addLeft(t2)
t2.addRight(t3)
t1.addRight(t4)
t2.addLeft(t5)
t2.addRight(t6)
t5.addLeft(t7)

'''
       1
    2     4
  5   6
7
'''

print(t1.height())
print(t1.is_balanced_BST())
