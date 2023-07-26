
# "sorted_list" is the sorted version of the list that desired to be sorted.

def bubble_sort(mylist):
    n = len(mylist)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if mylist[j]>mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1],mylist[j]
    
    return mylist    
    
mylist = [3, 6, 8, 10, 1, 2, 1, 2, 12, 16, 22, 1, 1, 2, 13, 3]
sorted_list=bubble_sort(mylist)

print(sorted_list)
