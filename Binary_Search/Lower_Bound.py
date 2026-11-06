nums = [1,1,2,2,2,3,3,5,6,7,7,7,8,8,9,10,11,11,12,13]

def LowerBound(nums, target):
    n = len(nums)
    lb = 1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
    return lb

print(LowerBound(nums, 11))