# def max_mirror(arr):
#     max_length = 0

#     for i in range(len(arr)):
#         for j in range(len(arr), 0, -1):
#             length = 0

#             while i + length < len(arr) and j - length - 1 >= 0 and arr[i + length] == arr[j - length - 1]:
#                 length += 1

#             max_length = max(max_length, length)

#     return max_length












def max_mirror(arr):
    max_length = 0

    for i in range(len(arr)):
        for j in range(len(arr), 0, -1):
            length = 0

            while i + length < len(arr) and j - length - 1 >= 0 and arr[i + length] == arr[j -length - 1]:
                length += 1

            max_length = max(max_length, length)
                
    return max_length

print(max_mirror([1, 2, 3, 8, 9, 3, 2, 1])) # 3
print(max_mirror([1, 2, 1, 4])) # 3
print(max_mirror([7, 1, 2, 9, 7, 2, 1])) # 2