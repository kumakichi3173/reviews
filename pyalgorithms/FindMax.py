# use a recursive algorithm to find a maximum value in a list of values
# 

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items): # a function, named find_max accept a list of numeric values 
    # breaking condition: last item in list? return it
    if len(items) == 1: # when the function is called, it will check to see if the list has only 1 item in it
        return items[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:]) # items[1:] means that the item at the index 1 to the "end"
    print(op2) # 87 will win all the time
    # print(op1, op2)

    # perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2


# test the function
print(find_max(items))
