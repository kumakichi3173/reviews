# demonstrate hashtable (an associative array)
# some languages call these as "dictionaries"
# benefit 1: hash function has an ability to uniquely map a given key to a specific value (ex. counters, filters, etc..)
# benefit 2: It's O(1), so it's efficient
# drawback 1: For small datasets, arrays are usually more efficient
# Hash tables don't order entries in a predictable way (might be spread out ramdomly in the system's memory)

'''
# create a hashtable all at once
items1 = dict({"key1": 1, "key2": 2, "key3": "three"}) # use a dict function
print(items1)

# create a hashtable progressively
items2 = {} # create an empty dictionary
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# try to access a nonexistent key (you will get an error message)
# print(items1["key6"])

# replace an item
items2["key2"] = "two"
print(items2)

# iterate the keys and values in the dictionary
for key, value in items2.items(): # this gives an item's list
    print("key: ", key, " value: ", value) # (key,..,value) is a format
'''

# more exercise

'''
# exercise 1
array = [1, 2, 3, 4, 5]
print(array)

for i in array:
    print (i, "yo")


# exercise 2
my_dict={} # my_dict is defined
my_dict["Jack"] = 26
my_dict["Annie"] = 21
my_dict["Bobby"] = 27
my_dict["Sifat"] = 22

for key, value in my_dict.items():
    print(key, value)

'''
my_dict = { 'Jack': 26, 'Annie': 21, 'Bobby': 27, 'Sifat': 22}
my_dict["Annie"] = 21
print(my_dict)

my_dict.clear() #clear the inside of the dictionary
print(my_dict)

