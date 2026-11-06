nums = [1, 2, 7, 8, 9, 3, 4, 5]

def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        max_index = i
        
        for j in range(i + 1, n):
            if nums[j] > nums[max_index]:
                max_index = j

        nums[i], nums[max_index] = nums[max_index], nums[i]

selection_sort(nums)
print(nums)