# use recursion to implement a countdown counter
# Using recursion to implement power and factorial functions
# Recursive functions need to have a breaking condition
# A breaking condition prevents infinite loops and eventual crashes
# Each time the function is called, the old arguments are saved (call stack)

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)


countdown(5)
