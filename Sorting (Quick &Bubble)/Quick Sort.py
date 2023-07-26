
# "list_needed" represents the list of elements that will be sorted.
# "pivot" is the middle element that seperates the list to 2 groups of elements as smaller elements and bigger elements.
# "smaller_ones" is the list of elements whose values are smaller than pivot value.
# "bigger_ones" is the list of elements whose values are bigger than pivot value.
# "middle_ones" is the list of elements whose values are equal to pivot value.
# "sorted_list" is the sorted version of the list that desired to be sorted.

def quicksort(list_needed):
    
    if len(list_needed) <= 1:
        return list_needed

    pivot = list_needed[len(list_needed)//2]
    smaller_ones = [i for i in list_needed if i < pivot] 
    middle_ones = [i for i in list_needed if i == pivot] 
    bigger_ones = [i for i in list_needed if i > pivot] 
    
    return quicksort(smaller_ones) + middle_ones + quicksort(bigger_ones)
    
list_needed = [3, 6, 8, 10, 1, 2, 1, 2, 12, 16, 22, 1, 1, 2, 13, 3]
sorted_list = quicksort(list_needed)

print(sorted_list)
