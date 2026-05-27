from heap import MaxHeap

def find_kth_smallest(nums, k):
    temp_heap = MaxHeap()
    for num in nums:
        temp_heap.insert(num)
        if len(temp_heap.heap) > k:
            temp_heap.remove()
    return temp_heap.remove()

# nums = [30,200,500,3,2]
k = 2

# print(f"This is the kth smallest number in {nums} : {find_kth_smallest(nums, k)}")

def max_stream(nums):
    heap = MaxHeap()
    lst = []
    for num in nums:
        heap.insert(num)
        lst.append(heap.heap[0])
    return lst

nums = [1,3,2,5,4]
# print(max_stream(nums))

# factorial of k 
# 4 = 4*3*2*1
def get_fact(k):
    if k == 1:
        return 1
    return k * get_fact(k-1)

print(get_fact(4))
    



