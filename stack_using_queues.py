from queue import Queue
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        print(__name__)

    def push(self,x):
        self.q2.put(x)

        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()
        self.q1,self.q2 = self.q2,self.q1

    def pop(self):
        if self.q1.empty():
            return None
        self.q1.get()

    def peek(self):
        return self.q1.queue[0]
        

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("top element is",s.peek())
    s.pop()
    print("top element is",s.peek())
    s.push(4)
    print("top element is",s.peek())
   