arr1= [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

a = len(arr1)
b = len(arr1[0])
c = len(arr2)
d = len(arr2[0])

arr3 = [[0]*d for _ in range(a)]



for i in range(a):
    for j in range(d):
        for k in range(c):
            arr3[i][j] += arr1[i][k] * arr2[k][j]

print(arr3)

# arr3[i][j] += arr1[i][k] * arr2[k][j]