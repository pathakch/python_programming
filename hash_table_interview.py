l1 = [1,2,5,2,3,5,1,1,2,5,5,5]
l2 = [4,7,5,4,7,5]

def find_match(list1, list2):
    d = {}
    for num in list1:
        d[num] = 1
    for key in list2:
        if key in d.keys():
            return key
    return False

# print(find_match(l1, l2))

# Question. 2. Find duplicates
l1 = [1,2,5,2,3,5]

def find_duplicates(lst):
    res = []
    d = {}
    for num in lst:
        if num in d:
            res.append(num)
        d[num] = True
    return res

# print(find_duplicates(l1))

# Question.3 Find first non repeating character in a given string
st = 'eetcode'

def find_first_non_repeating_char(letter):
    d = {}
    for char in letter:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    for key in d:
        if d[key] == 1:
            return key
    return None
        
# print(find_first_non_repeating_char(st))

# Question.4. find anagram list
strings = ['eat','ate','cat','tac','tea','act','bat']

def find_anagram(strings):
    anagram_list = {}
    for string in strings:
        cannonical = ''.join(sorted(string))
        if cannonical in anagram_list:
            anagram_list[cannonical].append(string)
        else:
            anagram_list[cannonical] = [string]
    return anagram_list.values()

# print(find_anagram(strings))

# Question.5. Two Sum - Interview Question
nums = [5, 1, 7, 2, 9, 3]
target = 10

def pairs_indices(nums, target):
    d = {}
    for idx, num in enumerate(nums):
        n = target - num
        if n in d:
            return list([d[n], idx])
        else:
            d[num] = idx
    return []

# print("pair indices list :", pairs_indices(nums, target))

# Question.6. Find starting and ending index of number in an array which sum to a target number
num_1 = [1,2,3,4,5]
target_1 = 9

def subarray_sum(nums, target):
    sum_index = {0:-1}
    current_sum = 0
    for idx, num in enumerate(nums):
        current_sum += num
        n = current_sum - target
        if n in sum_index:
            return list([sum_index[n]+1, idx])
        else:
            sum_index[current_sum] = idx
    return []

# print(subarray_sum(num_1, target_1))

# Question.7. remove duplicates from a list 
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]

def remove_duplicates(my_list):
    s = set()
    s.update(my_list)
    return list(s)

# Question. find pairs(one element from first list and second from second list) which add to a target
arr1 = [1, 2, 3, 5]
arr2 = [1, 3, 4, 5]
target_num = 6

def find_pairs(arr1, arr2, target):
    d = set(arr1)
    res = []
    for num in arr2:
        n = target - num
        if n in d:
            res.append((n, num))
    return res

# print(find_pairs(arr1, arr2, target_num))

# Question.8. 

def longest_consecutive_sequence(nums):
    s = set(nums)
    cnt = 0
    for num in nums:
     if num+1 in s or num-1 in s:
        cnt += 1
        
    return cnt

n = [100,1, 200,3,5,4,2,7,9,6]
print(longest_consecutive_sequence(n))

