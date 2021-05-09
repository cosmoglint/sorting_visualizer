# lst = [5,63,1,23,1,4,6,2,34,1]
#  This is a sorting algorithm I kinda thought of from the famous musician puzzle https://www.youtube.com/watch?v=vIdStMTgNl0&ab_channel=TED-Ed
#  The idea is to swap the elements which is found in the place till it matches its index. This only works on lists where the elements are 1 to len(lst) or in order without any breaks
lst = [6,9,4,0,5,3,1,2,8,7,10]


def check_swap(lst,index,value):
    if value == i:
        return lst
    else:
        lst[i] = lst[value]
        lst[value] = value
        return check_swap(lst,index,lst[i])


for value,i in enumerate(lst):
    lst = check_swap(lst,i,value)

print(lst)
