# try out the Python queue functions (ex. order processing or messaging)
# In Python, we can use a regular list to represent a stack and queue
# You can use a regular list as a queue in Python, but it's very inefficient to do so.. 
# ..b/c removing items from the front of a list requires a big O of of linear time complexity 
# ..b/c all the subsequent items have to be shifted down in their slots when you do that 
from collections import deque # deque module is way more efficient compared to a regular list 

# create a new empty deque object that will function as a queue
queue = deque() 

# add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print the queue contents
print(queue)

# pop (delete) an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)
