a = [10,23,44,35,23,1,53,21]

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(a)