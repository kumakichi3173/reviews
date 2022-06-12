def efun(num):
    if num == 0:
        return 1
        else:
        return num*efun(num-2)