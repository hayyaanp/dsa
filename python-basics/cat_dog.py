def cat_dog(s):
    cat = 0
    dog = 0

    for i in range(len(s)-2):
        if s[i] == 'c' and s[i+1] == 'a' and s[i+2] == 't':
            cat += 1
        if s[i] == 'd' and s[i+1] == 'o' and s[i+2] == 'g':
                    dog += 1

    return cat == dog

print(cat_dog("cat1catdog"))