def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j] < lst[i]:
                lst[j],lst[i] = lst[i], lst[j]
            else:
                continue
    return lst