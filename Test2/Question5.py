class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next

        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size

    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p
            self.tail =p
        self.size += 1

    def push_front(self, data):
        if self.isEmpty():
            self.head = self.tail = self.Node(data)
        else:
            p = self.Node(data, self.head)
            self.head = p
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self) :
        return self.size == 0

    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def removeDup(self):
        temp = self.head
        l = []
        l.append(temp.data)
        while temp.next != None:
            if temp.next.data not in l and temp.data != temp.next.data:
                l.append(temp.data)
                temp = temp.next
            else:
                temp.next = temp.next.next

    def contentEquivalence(self, n):
        if len(self) != len(n):
            return False

        s1 = set()
        s2 = set()
        for i in range(len(self)):
            s1.add(self.nodeAt(i).data)
        for i in range(len(n)):
            s2.add(n.nodeAt(i).data)
        return s1==s2

    def add(self, data):
        if self.isEmpty():
            self.append(data)
        else:
            newNode = self.Node(data)
            if newNode.data < self.head.data:
                self.push_front(data)
                return
            kk = self.head
            previous = None
            while kk is not None:
                if previous is not None:
                    if previous.data <= newNode.data <= kk.data:
                        newNode.next = kk
                        previous.next = newNode
                        self.size+=1
                        return
                previous = kk
                kk = kk.next
            self.append(data)

def findMode(list):
    mem = {}
    max = 0
    for i in range(len(list)):
        data = list.nodeAt(i).data
        if mem.get(data,0) == 0:
            mem[data]=1
        else:
            mem[data]+=1
        if mem.get(data,0) > max:
            max = mem.get(data,0)
    ans = LinkedList()
    for j in mem:
        if mem[j] == max:
            ans.append(j)
    if len(ans) > 3:
        print("Mode is not available.")
        return
    else:
        output = 'Mode = '
        for i in range(len(ans)):
            data = ans.nodeAt(i).data
            output += ' '+str(data)
        print(output)

numbers = list(map(int,input("Enter numbers : ").split()))
list = LinkedList()
for item in numbers:
    list.add(item)
print("Output :")
print(list)
print('Amount of data =',len(list))
findMode(list)