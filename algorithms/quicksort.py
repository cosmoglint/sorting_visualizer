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
