def valid_anagram(s: str, t: str):
    s_dict = dict()
    t_dict = dict()

    if len(s) != len(t):
        return False

    for i in s:
        if i not in s_dict:
            s_dict[i] = 0

        s_dict[i] += 1 

    for j in t:
        if j not in t_dict:
            t_dict[j] = 0

        t_dict[j] += 1

    
    return s_dict == t_dict



print(valid_anagram("racecar", "carrace")) # true
print(valid_anagram("jar", "jam")) # false
print(valid_anagram("x", "x")) # true
