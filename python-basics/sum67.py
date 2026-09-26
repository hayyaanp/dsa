def sum67(nums):
    flag = False
    sum = 0
    for n in nums:
        if n == 7:
            flag = True
        if n != 7 and not flag:
                    sum += n
        if n == 8:
            flag = False
    return sum

assert sum67([1, 2, 2]) == 5
assert sum67([1, 2, 2, 7, 99, 99, 8]) == 5
assert sum67([8, 2, 3, 7, 99, 1, 8, 3]) == 16

print("All test passed!")