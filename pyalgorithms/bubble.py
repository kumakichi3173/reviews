# Bubble sort algorithm


def bubbleSort(dataset):
    # start with the array length and decrement each time
    # length of the dataset -1 b/c that's the zero index array's last item
    # we stop at the zeroth item and step by -1 each time
    # count down from the end of the array
    for i in range(len(dataset)-1, 0, -1): 
        # examine each item pair (compare the neighboring elements and swap them if needs)
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting state: ", list1)
    bubbleSort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()