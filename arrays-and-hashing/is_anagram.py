def is_anagram(s, t):

    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in t:
        if char in count:
            count[char] -= 1
        else:
            return False

    for val in count.values():
        if val != 0:
            return False
        
    return True

print(is_anagram("anagram", "nagaram")) # true
print(is_anagram("rat", "car")) # false
