class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    
    def getH(self):
        if self.left and self.right:
            return 1+ max(self.left.getH(),self.right.getH())
        elif self.left:
            return  1+self.left.getH()
        elif self.right:
            return  1+ self.right.getH()
        else:
            return 0
    def getB(self):
        if self.left and self.right:
            return 1+ self.left.getB()+self.right.getB()
        elif self.left:
            return  1+self.left.getB()
        elif self.right:
            return  1+ self.right.getB()
        else:
            return 0

class Bst:
    def __init__(self):
        self.root = None
        self.countL=0
        self.countR=0
        self.check=0
    
    def insert(self,node):
        if self.root is None:
            self.root= node
        else:
            Rootnode=self.root
            while True:
                if node.data >= Rootnode.data:

                    if Rootnode.right is None :

                        Rootnode.right = node
                        

                        
                        break
                    Rootnode = Rootnode.right
                    self.countL+=1 
                else: 

                    if Rootnode.left is None:
                        Rootnode.left = node
                        
                        

                        break
                    Rootnode = Rootnode.left   
                    self.countL+=1           
    def HTree(self):
        if self.root:
            return self.root.getH()
        else:
            return 0
    
    def BTree(self):
        if self.root:
            return self.root.getB()-1
        else:
            return 0
    def PrintTree(self):
        def _PrintTree(node, level):
            if node != None:
                _PrintTree(node.right, level + 1)
                print('     ' * level, node)
                _PrintTree(node.left, level + 1)
        _PrintTree(self.root, 0)


kk=Bst()
print(" *** Binary Search Tree Height ***")
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = kk.insert(Node(i))
print('Height =  {0}'.format(kk.HTree()))