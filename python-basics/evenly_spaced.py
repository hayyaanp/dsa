def evenly_spaced(a, b, c):
    nums = sorted([a, b, c])

    return nums[1] - nums[0] == nums[2] - nums[1]

print(evenly_spaced(4, 6, 2))