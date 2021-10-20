class Stack:
    def __init__(self):
        self.item = []
    def push(self,data):
        return self.item.append(data)
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    def isEmpty(self):
        return self.size()==0
    def peek(self):
        if self.size()!=0:
            return self.item[-1]
    def __str__(self):
        kk = ''
        for i in self.item:
            kk+=str(i)+" "
        return "Data in Stack is : "+kk      
    def bottom(self):
        if self.size()!=0:
            return self.item[0]
s = int(input("Enter choice : "))
if s == 1:
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
elif s == 2:
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
elif s == 3:
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())