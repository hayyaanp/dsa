# def round_sum(a, b, c):

#     def round10(num):
#         rem = num % 10
#         if rem >= 5:
#             return num + (10 - rem)
#         else:
#             return num - rem
        
#     return round10(a) + round10(b) + round10(c)

# assert round_sum(16, 17, 18) == 60
# assert round_sum(12, 13, 14) == 30
# assert round_sum(6, 4, 4) == 10

# print("All test passed!")

def round_sum(a, b, c):

    def round(num):
        if num % 10 >= 5:
            return num + 10 - (num % 10)
        else:
            return num - (num % 10)

    return round(a) + round(b) + round(c)

print(round_sum(16, 17, 18))
print(round_sum(12, 13, 14))
print(round_sum(6, 4, 4))