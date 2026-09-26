# def splitArray(nums):
#     def splitArrayHelper(nums, index, sum1, sum2):
#         if index == len(nums):
#             return sum1 == sum2
        
#         if splitArrayHelper(nums, index + 1, sum1 + nums[index], sum2):
#             return True
        
#         if splitArrayHelper(nums, index + 1, sum1, sum2 + nums[index]):
#             return True

#         return False
    
#     return splitArrayHelper(nums, 0, 0, 0)












def split_array(nums):

    def split_array_helper(index, nums, sum1, sum2):
        if index == len(nums):
            return sum1 == sum2

        return split_array_helper(index+1, nums, sum1 + nums[index], sum2) or split_array_helper(index+1, nums, sum1, sum2 + nums[index])

    return split_array_helper(0, nums, 0, 0)




print(split_array([2, 2])) # true
print(split_array([2, 3])) # false
print(split_array([5, 2, 3])) # true
