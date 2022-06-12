# use recursion to implement a countdown counter
# Using recursion to implement power and factorial functions
# Recursive functions need to have a breaking condition
# A breaking condition prevents infinite loops and eventual crashes
# Each time the function is called, the old arguments are saved (call stack)

def countdown(x):
    # breaking condition
    if x == 0:
        print("Done!")
        return
    # Otherwise, recursion    
    else:
        print(x, "...")
        countdown(x-1)
        print("yo") # This is called after all the recurtions happened

countdown(5)
