
n, k = input().split()
n = int(n)
k = int(k)


numbers = input().split()
a = []
for i in range(n):
    a.append(int(numbers[i]))


for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp


print(a[k - 1])