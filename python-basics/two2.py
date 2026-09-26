def two2(nums):
    return [(num * 2) for num in nums if (num * 2) % 10 != 2]


print(two2([1, 2, 3])) # [4, 6]
print(two2([2, 6, 11])) # [4]
print(two2([0])) # [0]