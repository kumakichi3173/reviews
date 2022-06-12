def efun(num):
    if num == 0:
        return 1
    else:
        return num*efun(num-2)
#a = efun(8)
#print(a)

print(efun(8))