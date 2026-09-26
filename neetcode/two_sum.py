def two_sum(nums, target):

    indices = {}

    for i, n in enumerate(nums):
        indices[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indices and indices[diff] != 1:
            return [i, indices[diff]]

    return []

print(two_sum([3, 4, 5, 6], 7)) # [0, 1]
print(two_sum([4, 5, 6], 10)) # [0, 2]
print(two_sum([5, 5], 10)) # [0, 1]

