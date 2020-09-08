def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
                lst[j],lst[i] = lst[i], lst[j]
            else:
                continue
    return lst


def split(lst,low,high):
    pivot = lst[low]
    p1 = low+1
    p2 = high
    while True:
        while p1<=p2 and lst[p1]<=pivot:
            p1+=1
        while p1<=p2 and lst[p2]>=pivot:
            p2-=1
        if p1<=p2:
            lst[p1],lst[p2] = lst[p2],lst[p1]
        else:
            break
    lst[low],lst[p2] = lst[p2],lst[low]
    return p2


def seed(lst,low,high):
    if low>=high:
        return lst
    p = split(lst,low,high)
    seed(lst,low,p-1)
    seed(lst,p+1,high)

def quicksort(lst):
    seed(lst,0,len(lst)-1)
    return lst


def selectionsort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min]:
                min = j
        lst[i],lst[min]=lst[min],lst[i]

    return lst

def insertionsort(lst):
    for i in range(1,len(lst)):
        curval = lst[i]
        z = i-1
        while curval < lst[z] and z>=0:
            lst[z+1] = lst[z]
            z -= 1
        lst[z+1] = curval
    return lst

def mergesort(lst):
    length = len(lst)
    if length>1:
        L = (lst[:length//2])
        R = (lst[length//2:])
        L = mergesort(L)
        R = mergesort(R)

        lst = []

        while len(L)>0 and len(R) > 0:
            if L[0]<R[0] :
                lst.append(L.pop(0))
            else:
                lst.append(R.pop(0))
        for i in L:
            lst.append(i)
        for i in R:
            lst.append(i)
    return lst

arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

# print(quicksort(arr))
# print(selectionsort(arr))
# print(insertionsort(arr))
print(mergesort(arr))