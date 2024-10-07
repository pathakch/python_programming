a = [4,9,12,0,5,8]


for i in range(len(a)-1):
    min_idx = i
    for j in range(i+1, len(a)):
        if a[min_idx] > a[j]:
            min_idx = j 
    temp = a[min_idx]
    a[min_idx] = a[i]
    a[i] = temp 
print(a)