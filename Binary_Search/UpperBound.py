nums = [1,1,1,2,2,3,3,3,4,4,5,6,7,8,9,9,10,11,11,12,13,13]

def UpperBound(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high )//2
        if nums[mid] <= target:
            ub = mid
            low = mid + 1
        else:
            high = mid - 1
    return ub

print(UpperBound(nums, 11))