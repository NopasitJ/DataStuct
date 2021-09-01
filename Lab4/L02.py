class Queue:
    def __init__(self):
        self.item = list()

    def enqueue(self, value):
        self.item.append(value)

    def peek(self):
        if not self.is_empty():
            return self.item[0]
        else:
            return -1

    def stype(self, value):
        if self.is_empty():
            self.item.append(value)
        elif self.peek()[0] == 'EN':
            self.item.insert(0, value)
        else:
            for i in range(self.size()):
                if self.item[i][0] == 'EN':
                    self.item.insert(i, value)
                    return
            self.item.append(value)

    def size(self):
        return len(self.item)

    def is_empty(self):
        return self.size() <= 0

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            return -1

    def __str__(self):
        output = ""
        if not self.is_empty():
            for item in self.item:
                output += str(item) + ' '
        else:
            output = 'Empty'
        return output

inp = input('Enter Input : ').split(',')
q = Queue()
for i in inp:
    kk = i.split()
    if len(kk) == 1:
        if not q.is_empty():
            print(q.dequeue()[1])
        else:
            print('Empty')
    else:
        if kk[0] == 'EN':
            q.enqueue((kk[0], kk[1]))  
        elif kk[0] == 'ES':  
            q.stype((kk[0], kk[1]))