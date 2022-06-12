# with the sorted list, we can use a technique, a binary search
# searching for an item in an ordered list
# executes in the logarithmic time scale O(log n)
# everytime the list doubles in size, you only have to perform a couple if extra operations


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist): # uses 2 arguments, item and itemlist(list)
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    # the while loop keeps excuting in which case we know that the value doesn't exist
    while lowerIdx <= upperIdx:
        # calculate the middle point
        midPt = (lowerIdx + upperIdx)// 2

        # if item is found, return the index
        if itemlist[midPt] == item: # this if state means that "if the itemlist at the midpoint is equal to the item"
            return midPt
        # otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print("the index of 23 is", binarysearch(23, items))
print("the index of 87 is", binarysearch(87, items))
print("the index of 250 is", binarysearch(250, items))
