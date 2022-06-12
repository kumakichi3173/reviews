# divide and conquer algorithm
# breaks a dataset into individual pieces and merges them
# users recusion to operate on dataset
# performs well on large set of data
# In general has a performance of O(n log n) time complexity

# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

# the code starts by taking the dataset argument
def mergesort(dataset):
    # if the elements are more than 2, it keeps breaking down into smaller and smaller pieces
    if len(dataset) > 1: # it keeps going until the length become 1
        mid = len(dataset) // 2 # spread into 2 arrays (find the midpoint of the original dataset, so around between 56 and 23)
        leftarr = dataset[:mid] # break into the left array
        rightarr = dataset[mid:] # break into the right array

        # recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)
