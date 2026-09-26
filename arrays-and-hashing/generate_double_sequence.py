def generate_double_sequence(nums):
    ans = [0] * (2 * len(nums))
    for i in range(len(nums)):
        ans[i] = nums[i]
        ans[i + len(nums)] = nums[i]

    return ans


print(generate_double_sequence([1, 2, 1])) # [1, 2, 1, 1, 2, 1]
print(generate_double_sequence([1,3,2,1])) # [1,3,2,1,1,3,2,1]
