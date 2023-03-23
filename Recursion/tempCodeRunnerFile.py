def binary_sort(li, key):
    start = 0
    end = len(li)-1
    while start<=end:
        mid = (start+end)//2
        if li[mid] == key:
            return mid
        elif li[mid] > key:
            end = mid-1
        else:
            start = mid-1
    return -1 


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
print(binary_sort(li, n))