# Using recursion to implement power and factorial functions
# Recursive functions need to have a breaking condition
# A breaking condition prevents infinite loops and eventual crashes
# Each time the function is called, the old arguments are saved (call stack)

# 2^4 = 2*2*2*2 = 16
def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0: # breaking condition
        return 1
    else:
        return num * power(num, pwr-1)

# 0! = 1
# 5! = 5*4*3*2 = 120
def factorial(num):
    if (num == 0): # breaking condition
        return 1
    else:
        return num * factorial(num-1)

print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))

