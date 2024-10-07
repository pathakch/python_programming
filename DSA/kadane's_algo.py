#************************************* Kadane's Algorithm ************************ ##########################
def kadane_dsa(arr,size):
    """
    returns maximum sum of sub array containing contiguos element
    """
    max_so_far = float('-inf') # outputs negative infinity (o/p : = -inf) meaning we wanted to get most negative element
    max_ending_here = 0

    for i in range(0,size):
        max_ending_here = max_ending_here+arr[i]
        if max_so_far < max_ending_here:
            max_so_far=max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
    
arr = [-2,-3,4,-1,-2,1,5,-3]      
# print("Maximum contiguous Sum : ",kadane_dsa(arr, len(arr))) 

#********************************* function to print maximum sum sub array****************
from sys import maxsize # it o/p maximum integer in python interpreter

def maxSumSubArray(arr,size):
    max_so_far = -maxsize-1
    max_ending_here = 0
    start = 0
    s=0
    end = 0
    for i in range(0,size):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    return arr[start:end+1]
print("This is sub Array of maximum Sum : ",maxSumSubArray(arr, len(arr)))       



