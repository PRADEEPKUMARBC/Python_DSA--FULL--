num = [9, 3, 2, 8, 5, 1, 4, 6, 7]

def reverse(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left + 1, right - 1)

print(reverse(num, 0, len(num) - 1))
print(num)

num = [9, 3, 2, 8, 5, 1, 4, 6, 7]

def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            return arr
print(reverse(num, 0, len(num) - 1))
print(num)