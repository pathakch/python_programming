#take two sosrted list, 
#run while loop to compare, i from list1 and j from list2 , till any one of list runs out of index
#run one while loop to insert remaining data from the lost which is not run out of index

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

def merge_list(list1, list2):
    combined = []
    i = j = 0
    while i < len(list1) and j < len(list2):
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

l1 = [1,4,9,10]
l2 = [3,7]

# print(merge_list(l1, l2))

def merge_sort(lst):
    # check the lenght of list if i's 1 then return
    if len(lst) == 1:
        return lst
    # if length not one then break the list until it's length is 1 by calling recursive function
    mid_idx = int(len(lst)/2)
    left = merge_sort(lst[: mid_idx])
    right = merge_sort(lst[mid_idx :])
    # call helper function passing the list of length one
    res = merge_list(left, right)
    # retrun 
    return res

l3 = [90,50,1,5,100,80]
print(merge_sort(l3))
    