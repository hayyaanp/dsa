def isEverywhere(nums, val):
    for i in range(len(nums)-1):
        if nums[i] != val and nums[i+1] != val:
            return False
    return True


print(isEverywhere([1, 2, 1, 3], 1)) # true
print(isEverywhere([1, 2, 1, 3], 2)) # false
print(isEverywhere([1, 2, 1, 3, 4], 1)) # false