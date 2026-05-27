
def merge(list1, list2):
    combined = []
    i = j = 0
    while i < len(list1)  and j < len(list2) :
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined

#create merge_sort function , use recursion to break down list till th list length reaches to 1 , 
#if length is 1 then return the function
# call helper function once left and right reaches to length 1

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid_idx = int(len(lst)/2)
    left = merge_sort(lst[: mid_idx])
    right = merge_sort(lst[mid_idx :])

    final_lst = merge(left, right)
    return final_lst

lst = [8,6]
print(merge_sort(lst))
