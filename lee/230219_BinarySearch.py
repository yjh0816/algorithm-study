# 1
n, k = 4, 6
arr = [19, 15, 10, 17]

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        for i in arr:
            temp_arr[i] = arr[i] - mid
            # not yet..
        
    

# 2
from bisect import bisect_left, bisect_right
n, k = 7, 2
arr = [1, 1, 2, 2, 2, 2, 3]

count = bisect_right(arr, k) - bisect_left(arr, k)
print(count)