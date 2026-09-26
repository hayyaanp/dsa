def scores_clump(scores):
    adjacent_count = 0
    for i in range(len(scores)-1):
        for j in range(i+1, len(scores)):
            if scores[j] - scores[i] <= 2:
                adjacent_count += 1
    return adjacent_count >= 3

print(scores_clump([3, 4, 5])) # true
print(scores_clump([3, 4, 6])) # false
print(scores_clump([1, 3, 5, 5])) # true