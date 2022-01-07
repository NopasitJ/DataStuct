class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    if l == [] :
        return node(None)
    else:
        h = node(l[0])
        t = h
        for i in range(1,len(l)):
            t.next = node(l[i])
            t = t.next
        return h

def printList(H):
    li = []
    temp = H
    if temp != None:
        while temp.next != None:
            li.append(temp.data)
            temp = temp.next
        li.append(temp.data)
        print(*li)
    
def mergeOrdersList(p,q):
    li = []
    temp1 = p
    temp2 = q
    while temp1 != None:
        if temp2 != None:
            if temp1.data < temp2.data:
                li.append(temp1.data)
                temp1 = temp1.next
            elif temp1.data > temp2.data:
                li.append(temp2.data)
                temp2 = temp2.next
            else:
                li.append(temp1.data)
                li.append(temp2.data)
                temp1 = temp1.next
                temp2 = temp2.next
        else:
            li.append(temp1.data)
            temp1 = temp1.next
    while temp2 != None:
        li.append(temp2.data)
        temp2 = temp2.next
    return createList(li)

inp = input("Enter 2 Lists : ").split('/')
L1 = [int(e) for e in inp[0].split(',')]
L2 = [int(e) for e in inp[1].split(',')]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrdersList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)