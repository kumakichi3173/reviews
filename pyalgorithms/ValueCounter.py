# using a hashtable to count individual items
# this code is the updated ver. of filter.py
# this code contains one instance each of the item names with the associated values that represent the counts of each type

# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable object to hold the items and counts
counter = dict()

# iterate over each item and increment the count for each one
for item in items: # for each loop
    if item in counter.keys(): # if the item already exists in this set of keys, you just need to add one to the value that is assosiated to the key
        counter[item] += 1
    else:
        counter[item] = 1 # Initialize the item b/c we are encountering the item for the first time

# print the results
print(counter) # print out the contents of the counter
