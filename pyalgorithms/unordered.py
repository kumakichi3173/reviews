# searching for an item in an ordered list
# this technique uses a binary search

# declare a list of values to operate on
# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

# for this method, we have to find the item one by one 
def find_item(item, itemlist):
    for i in range(len(itemlist)):
        if item == itemlist[i]:
            return i 
    
    return None


print("the index of the item, 87 is", find_item(87, items))
print("the index of the item, 250 is", find_item(250, items))
