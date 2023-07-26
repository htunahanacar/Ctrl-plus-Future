
# *high* stands for the last element's position which is n-1 in a list.
#* low* stands for the first element's position which is 0 in a list.
# Mid stands for the middle element's position in a list.
# Target is the number that we want to searce in a list whether it exists or not.

def binary_ite(list_needed, low, high, target):
    while high>=low:
        mid = (high+low)//2
        if target==list_needed[mid]:
            return "Target is found."
        elif target>=list_needed[mid]:
            low = mid+1
        else: # target<=list_needed[mid]
            high = mid-1
    return "Target is not found."       

list_needed = [2, 4, 6, 8, 10, 12, 14, 16]

result = binary_ite(list_needed, 0, len(list_needed)-1, 4)
print(result)
