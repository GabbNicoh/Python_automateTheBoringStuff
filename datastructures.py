class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
            
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
        
    def __str__(self):
        return str(self.stack)
    
stack = Stack()
for i in range(1, 5):
    stack.push(i)
print(stack.__str__())
print(stack.pop())
print(stack.stack)
print(stack.peek())

from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.popleft()

    def __str__(self):
        return str(self.queue)

queue = Queue()
for i in range(10):
    queue.enqueue(i)

print(queue.queue)
print(queue.dequeue())
print(queue.queue)

class MaxHeap():
    def __init__(self):
        super().__init__
        MaxHeap.maxheap[0] = 0
        