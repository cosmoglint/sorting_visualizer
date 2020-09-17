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