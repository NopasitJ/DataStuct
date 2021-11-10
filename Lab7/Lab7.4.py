class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while(1):
                if data < cur.data:
                    if cur.left != None:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        return self.root
                else:
                    if cur.right != None:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        return self.root

    def preOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.inOrder(node.left)
            print(node.data, end=" ")
            self.inOrder(node.right)

    def postOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=" ")

    def breadth(self):
        l = list()
        l.append(self.root)
        while l:
            n = l.pop(0)
            print(n, end=" ")
            if n.left:
                l.append(n.left)
            if n.right:
                l.append(n.right)


S = Bst()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = S.insert(i)
print("Preorder : ", end="")
S.preOrder()
print("\nInorder : ", end="")
S.inOrder()
print("\nPostorder : ", end="")
S.postOrder()
print("\nBreadth : ", end="")
S.breadth()
