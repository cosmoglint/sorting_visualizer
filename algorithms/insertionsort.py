def insertionsort(lst):
    for i in range(1,len(lst)):
        curval = lst[i]
        z = i-1
        while curval < lst[z] and z>=0:
            lst[z+1] = lst[z]
            z -= 1
        lst[z+1] = curval
    return lst