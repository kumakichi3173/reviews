# Find the greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a, b):
    # pass
    while (b != 0):
        t = a # t is a variable and used as a temp
        a = b # set a equal to b
        b = t % b # divide t (which is a) by b

    return a # if we find the GCD, then stop

# try out the function with a few examples
# change the values to get GCD
print(gcd(60, 96)) # should be 12
print(gcd(20, 8)) # should be 4