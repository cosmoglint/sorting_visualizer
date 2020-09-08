import generator
import algorithms.algorithms


list_length = int(input("enter length of list"))

list_to_sort = generator.gen_list(list_length,list_length)

print(list_to_sort)
print(algorithms.algorithms.bubblesort(list_to_sort))