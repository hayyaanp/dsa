# def insertion_sort(nums):

#     for i in range(len(nums)):
#         cur = nums[i]
#         while i > 0 and i < len(nums) and cur < nums[i - 1]:
#             temp = nums[i - 1]
#             nums[i - 1] = cur
#             nums[i] = temp
#             i -= 1
#             print(nums)

#     return nums


def insertion_sort(nums):

    for j in range(len(nums)):
        key = nums[j]
        i = j - 1
        while i >= 0 and nums[i] < key:
            nums[i + 1] = nums[i]
            i -= 1
        nums[i + 1] = key

    return nums

print(insertion_sort([5, 2, 4, 6, 1, 3])) # [1, 2, 3, 4, 5, 6]
