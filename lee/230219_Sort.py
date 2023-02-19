n, k = 5, 3
a = [1, 2, 5, 4, 4]
b = [5, 5, 6, 6, 5]

a.sort()
b.sort(reverse=True)
print(a, b)
for i in range(k):
    if b[i] > a[i]:
        b[i], a[i] = a[i], b[i]

print(sum(a))