from curses.ascii import isalpha
from queue import Empty


class Conversion:
    def __init__(self,n):
        self.top = -1
        self.n = n
        self.array = []
        self.output = []
        self.precedence = {
                            "+":1,
                            "-":1,
                            "*":2,
                            "/":2,
                            "^":3
        }
        
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top += 1
        self.array.append(op)

    def isOperand(self,ch):
        # if ch.isalpha()==True:
        #     return True
        # return False
        return ch.isalpha()

    def lowerPrecedence(self,i):
        try:
            if self.precedence[i] <= self.precedence[self.peek()]:
                return True
            return False
        except KeyError:
            return False
        
    def infixToPostfix(self,exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == "(":
                self.push(i)
            elif i == ")":
                while ((not self.isEmpty()) and self.peek()!="("):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek()!="("):
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty() and self.lowerPrecedence(i)):
                    a = self.pop()
                    self.output.append(a)
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        print("".join(self.output))


exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)

