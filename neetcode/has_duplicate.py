def has_duplicate(nums):

    my_dict = dict()

    for num in nums:
        if num not in my_dict:
            my_dict[num] = 0
        
        my_dict[num] += 1

        if my_dict[num] > 1:
            return True

    return False


print(has_duplicate([1, 2, 3, 3])) # true
print(has_duplicate([1, 2, 3, 4])) # false