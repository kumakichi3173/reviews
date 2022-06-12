# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # using the all function, which is in boolian, 
    # it results in returning true or false after checking every item in this collection evaluates to either true or false 
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    # using the brute force method
    # for i in range(0, len(itemlist)-1):
    #     if (itemlist[i] > itemlist[i+1]): # if at any point the following number violate the abave rule, then we know the list is unsorted
    #         return False 
    # therefore, False
    # return True

print(is_sorted(items1))
print(is_sorted(items2))

