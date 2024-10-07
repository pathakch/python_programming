a = [5,9,0,1,8,3,6]

# a = [2,8,9,2]

for i in range(len(a)-1, 0, -1):
    for j in range(i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)