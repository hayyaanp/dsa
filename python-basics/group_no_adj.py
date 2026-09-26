# def group_no_adj(start, nums, target):

#     def group_no_adj_helper(index, nums, sum1, sum2, target):
                
#         if index >= len(nums):
#             return sum1 == target or sum2 == target
        
#         group1 = group_no_adj_helper(index+2, nums, sum1 + nums[index], sum2, target)
#         group2 = group_no_adj_helper(index+2, nums, sum1, sum2 + nums[index], target)

#         return group1 or group2
    
#     return group_no_adj_helper(start, nums, 0, 0, target) or group_no_adj_helper(start+1, nums, 0, 0, target)

def group_no_adj(start, nums, target):

    if target == 0:
        return True

    if start >= len(nums):
        return False

    if group_no_adj(start + 2, nums, target - nums[start]):
        return True

    if group_no_adj(start + 1, nums, target):
        return True

    return False


print(group_no_adj(0, [2, 5, 10, 4], 12)) # true
print(group_no_adj(0, [2, 5, 10, 4], 14)) # false
print(group_no_adj(0, [2, 5, 10, 4], 7)) # false
print(group_no_adj(0, [2, 4, 6, 8], 10)) # true
