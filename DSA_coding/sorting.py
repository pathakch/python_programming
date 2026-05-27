l = [4,2,6,5,1,3]

def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                my_list[j+1], my_list[j] = my_list[j], my_list[j+1]
    return my_list

# print(f"Output of Bubble sort : {bubble_sort(l)}")

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        if i != min_idx:
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list

# print(f"Output of Selection sort : {selection_sort(l)}")

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            temp = my_list[j+1]
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

# print(f"Output of Insertion sort : {insertion_sort(l)}")

'''
Below is the helper function for merge sort, This function takes two sorted list and combine them to get the sorted list
'''
def merge(list1, list2):
    i = j = 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i = i+1
        else:
            res.append(list2[j])
            j = j+1
    while i < len(list1):
        res.append(list1[i])
        i = i+1
    while j < len(list2):
        res.append(list2[j])
        j = j+1
    return res
'''
Below is the actual merge sort function which takes unsorted list and make it sorted, 
Process - it divide the list into two halves left and right
and return left and right part of the divided list, again take those left and right part and again divide them into two halves
this process continues until left and right becomes one digit list, and then it passes theseleft and right parts into merge helper function
since they are one digit list so they are already sorted so helper function merge takes them combine them and return the sorted list
This function uses recursion and can be understood using call stack picture and process.
'''
def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    mid_idx = int(len(input_list)/2)
    left = merge_sort(input_list[:mid_idx])
    right = merge_sort(input_list[mid_idx:])
    return merge(left, right)

input_list = [3,1,100,5,2,10,0,4]
# print(merge_sort(input_list))

# Quick Sort:
def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[pivot_index] > my_list[i]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, start, end):
    if start < end:
        pivot_index = pivot(my_list, start, end)
        quick_sort_helper(my_list, start, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, end)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

    
my_list = [4,6,1,7,3,2,5]
print(quick_sort(my_list))

