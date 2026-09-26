def make_chocolate(small, big, goal):
    max_big_bars = min(big, goal // 5)
    remaining_goal = goal - (max_big_bars * 5)

    if remaining_goal <= small:
        return remaining_goal
    
    return -1


print(make_chocolate(4, 1, 9)) # 4
print(make_chocolate(4, 1, 10)) # -1
print(make_chocolate(4, 1, 7)) # 2