def count_identical_pairs(nums):
    my_dict = dict()
    count = 0
    for num in nums:
        if num in my_dict:
            count += my_dict[num]
            my_dict[num] += 1
        else:
            my_dict[num] = 1


    return count


print(count_identical_pairs([1,2,3,1,1,3])) # 4
print(count_identical_pairs([1,1,1,1])) # 6
print(count_identical_pairs([1,2,3])) # 0
