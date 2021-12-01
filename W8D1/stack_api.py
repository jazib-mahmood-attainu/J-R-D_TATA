stack = list()

def push(x):
    global stack
    stack.append(x)

def pop():
    global stack
    if isEmpty():
        return "No elements in stack"
    return stack.pop()

def peek():
    global stack
    if isEmpty():
        return "No elements in stack"
    return stack[-1]

def isEmpty():
    global stack
    return len(stack)==0

push(10)
push(5)
push(77)
print(stack)
pop()
print(stack)
# print(f"element removed was {r}")
print(peek())
pop()
print(peek())
pop()
print(peek())

print(isEmpty())



