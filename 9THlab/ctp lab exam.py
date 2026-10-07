from  dataclasses import dataclass
from typing import TypeVar, Generic
T= TypeVar("T")

@dataclass
class Request:
    id:int
    name:str
class Stack(Generic[T]):
    def __init__(self):
        self.items = []

    def push(self, x: T):
        self.items.append(x)

    def pop(self):
        if not self.items:
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if not self.items:
            return "Stack is empty"
        return self.items[-1]

class Queue(Generic[T]):
    def __init__(self):
        self.items = []

    def enqueue(self, x: T):
        self.items.append(x)

    def dequeue(self):
        if not self.items:
            return "Queue is empty"
        return self.items.pop(0)

    def front(self):
        if not self.items:
            return "Queue is empty"
        return self.items[0]

r1 = Request(1, "Harshi")
r2 = Request(2, "abhi")

q = Queue[Request]()
q.enqueue(r1)
q.enqueue(r2)

print("Queue Front:", q.front())
print("Dequeue:", q.dequeue())

s = Stack[Request]()
s.push(r1)
s.push(r2)

print("Stack Peek:", s.peek())
print("Pop:", s.pop())