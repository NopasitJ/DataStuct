class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def enQueue(self,i):
        self.item.append(i)
        return "Add " + i + " index is " + str(self.size()-1)

    def deQueue(self):
        if not self.isEmpty():
            temp = self.item[0]
            self.item.pop(0)
            return "Pop " + temp + " size in queue is " + str(self.size())
        return -1
    
    def peek(self):
        if not self.isEmpty():
            return self.item[0]
        return -1

Inp = input('Enter Input : ').split(',')
Q = Queue()
for i in Inp:
    kk = i.split()
    if kk[0] == 'E':
        temp = kk[1]
        print(Q.enQueue(temp))
    elif kk[0] == 'D':
        print(Q.deQueue())
if Q.size()==0:
    print("Empty")
else:
    print("Number in Queue is : ",str([x for x in Q.item]))
