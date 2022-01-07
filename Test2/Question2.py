class Queue :
    def __init__(self):
        self.data = []
    def __str__(self):
        if self.isEmpty() == True:
            
            return 'Empty Queue'
        kk = ''
        for i in self.data:
            kk+=str(i)+' '
        return 'Queue data : '+ kk
    def __len__(self) :
        return self.size()
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.size()==0
    def enQueue(self, new_data):
        return self.data.append(new_data)
    def deQueue(self):
        if self.isEmpty():
            return 'empty'
        return self.data.pop(0)
s = int(input('Enter choice : '))

if s==1:
    q1 = Queue()
    q1.enQueue(10)
    q1.enQueue(20)
    q1.enQueue(30)
    print(q1)
    q1.deQueue()
    q1.enQueue(40)
    print("Size of Queue :",len(q1))
    print(q1)
elif s==2:
    q1 = Queue()
    q1.enQueue(100)
    q1.enQueue(200)
    q1.enQueue(300)
    q1.deQueue()
    print(q1)
    print("Queue is Empty :",q1.isEmpty())
elif s==3:
    q1 = Queue()
    q1.enQueue(11)
    q1.enQueue(22)
    q1.enQueue(33)
    q1.deQueue()
    q1.deQueue()
    q1.deQueue()
    print(q1)
    print("Size of Queue :",len(q1))
    print("Queue is Empty :",q1.isEmpty())