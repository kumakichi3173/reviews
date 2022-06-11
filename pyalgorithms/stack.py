# stack is generaly used for "back" in a weebpage (backtracking)
# In Python, we can use a regular list to represent a stack and queue
# try out the Python stack functions

# create a new empty stack
stack = [] # make an empty list

# push items onto the stack
# append function, which is the list type supports, can add items to the stack (some other languages use the push function)
# push 4 items (integers) into the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the stack contents
print(stack)

# pop (remove) an item off the stack
x = stack.pop()
print(x)
print(stack)
