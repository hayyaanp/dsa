def check_sequence(s, t):

    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

print(check_sequence("abc", "ahbgdc")) # true
print(check_sequence("axc", "ahbgdc")) # false
