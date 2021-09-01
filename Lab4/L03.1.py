class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,new_data):
        self.items.append(new_data)
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.size() == 0
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return -1
    def head(self):
        if not self.is_empty():
            return self.items[0]
        return -1

q = Queue()
token = list(input('Enter code,hint : '))
diff = ord(token[-1])-ord(token[0])
token.pop()
token.pop()
for i in token:
    q.enqueue(chr(ord(i)+diff))
    print(q.items)