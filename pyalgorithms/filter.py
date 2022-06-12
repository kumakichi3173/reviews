# use a hashtable to filter (remove) out duplicate items from the list
# time complexity of this algorithm is 
# b/c it passes through each item and attempt to perform an addition to the hash table, which represents one unit of time  
# as the number of items in the list grows, the time complexity of this algorithm will grow in a linear fashion, O(n)

# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable to perform a filter
filter = dict()

# loop over each item and add to the hashtable
for item in items:
    filter[item] = 0 # set it as equaling to 0 b/c not using it

# create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)
