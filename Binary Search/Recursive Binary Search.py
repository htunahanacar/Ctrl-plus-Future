
# *high* stands for the last element's position which is n-1 in a list.
#* low* stands for the first element's position which is 0 in a list.
# Mid stands for the middle element's position in a list.
# Target is the number that we want to searce in a list whether it exists or not.

def binary_rec(list_needed, low, high, target):
    #The fuction created for recursive binary research. 
    if high >= low:

        mid= (high+low)//2
        if target==list_needed[mid]:
            return "Target is found."
        elif target>=list_needed[mid]:
            return binary_rec(list_needed, mid+1, high, target)
        elif target<=list_needed[mid]:
            return binary_rec(list_needed, low, mid-1, target)
        else:
            return "Something unexpected happened. Please contact the coder."
         
    else:
        return "Target is not found"
   
list_needed = [2, 4, 6, 8, 10, 12, 14, 16]

result = binary_rec(list_needed, 0, len(list_needed)-1, 6)
print(result)
