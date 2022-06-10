# Find the greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a, b):
    # pass
    while (b != 0):
        t = a # t is a variable
        a = b
        b = t % b

    return a # if we find the GCD, then stop

# try out thefunction with a few examples
print(gcd(60, 96)) # should be 12
print(gcd(20, 8)) # should be 4