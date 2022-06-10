# Linked list example


# the Node class
# a simple class that stores a single data field, called "val"
class Node(object):
    def __init__(self, val):
        self.val = val # a single data field, called "val"
        self.next = None # there is only one single field, called "next" which indicates that this is a single linked list

    def get_data(self): # getting data field      
        return self.val

    def set_data(self, val): # setting data field
        self.val = val

    def get_next(self): # next field pointer
        return self.next

    def set_next(self, next): # next field pointer
        self.next = next


# the LinkedList class
# linked list class itself is "next"
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head # there are already fields for the head
        self.count = 0 # a count field that keeps track for how many nodes they are in list

    def get_count(self): 
        return self.count

    # insert a new node
    def insert(self, data):
        new_node = Node(data)  # insert a new node into the list
        new_node.set_next(self.head) # that is going to be the current head of this list
        self.head = new_node # tells the head to point to the new node
        self.count += 1 # counting up by +1 (update the count)

    # find the first item with a given value
    # iterate over the node until we find the first one that has the matching data argument 
    def find(self, val):
        item = self.head # the code starts from the head of the node
        while (item != None):
            if item.get_data() == val: # if item get data function returns with the value that we are looking for then return "item" 
                return item
            else: # Otherwise, get the next item by "item.get_next()"
                item = item.get_next()
        return None

    # delete an item at given index 
    def deleteAt(self, idx):
        # checks if the current index is within the number of existing nodes in the list
        if idx > self.count: # If we give it an index that is more than what we currently have, we just simply return
            return
        if self.head == None:
            return
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self): # a utility that prints the contents of the lists
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)

itemlist.dump_list() # prints out the list using the dump list function

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13)) # find function to find some data in the list (in this case, 13 which is in the list)
print("Finding item: ", itemlist.find(78)) # find function to find some data in the list (in this case, 78 which is NOT in the list)

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()
