# https://leetcode.com/problems/implement-queue-using-stacks/
# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

class MyQueue:
    def __init__(self):
        self.main = []
        self.second = []

    def push(self, x: int) -> None:
        self.main.append(x)
        print(self.main)
        
    def pop(self) -> int:
        size = len(self.main)
        size2 = size - 1
        while size:
            self.second.append(self.main.pop())
            size = size - 1
        op = self.second.pop()
        while size2:
            self.main.append(self.second.pop())
            size2 = size2 - 1
        return op
        
    def peek(self) -> int:
        if len(self.main) == 0:
            return None
        return self.main[0]
        
    def empty(self) -> bool:
        if len(self.main) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)