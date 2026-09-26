def make_bricks(small, big, goal):
    max_big_bricks = goal // 5
    max_small_bricks = goal - (max_big_bricks * 5)

    return max_big_bricks <= big and max_small_bricks <= small

print(make_bricks(3, 1, 8)) # True
print(make_bricks(3, 1, 9)) # False
print(make_bricks(3, 2, 10)) # True
