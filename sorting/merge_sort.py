"""
Merge sort concept :
we will create a helper function which takes two sorted list and merge those list and return the final
sorted list , for example if l1 = [1,2,3] and l2 = [4,5,6] if we pass these two lists to helper function
it will return  l3 = [1,2,3,4,5,6]
Now what is the use of this helper function in merge sort and how it works to achieve merge sort
let's discuss below
let's say we have a list [4,8,2,5,7,9] and we want to sort it with merge sort
Merge sort concept : we will break this list in half which will give two list left_list = [4,8,2] and 
right_list = [5,7,9] , will break these two lists again and will get [4],[8,2],[5],[7,9] further will break these lists
untill we have only one element in each lists
finally we will get like this [4],[8],[2],[5],[7],[9] now these all lists are sorted in itself because 
they contain one one element , now we will pass all these lists in our helper function 2 at a time together
"""
def merge_fn(list1, list2):
    i = j = 0
    combined = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        elif list1[i] >= list2[j]:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

l1 = [1,8,9,10]
l2 = [4,8,9]
# print(merge_fn(l1, l2))

l3 = [20,4,8,10,5,7,9]

def sort_fn(lst):
    mid_idx = int(len(lst)/2)
    if len(lst) == 1:
        return lst
    left = lst[:mid_idx]
    right = lst[mid_idx:]
    sorted_left = sort_fn(left)
    sorted_right = sort_fn(right)
    return merge_fn(sorted_left, sorted_right)

print(sort_fn(l3))