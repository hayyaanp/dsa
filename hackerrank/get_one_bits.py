def get_one_bits(n):
    bits = list(bin(n)[2:])
    location = [0]
    for index, value in enumerate(bits, start=1):
        if value == "1":
            location[0] += 1
            location.append(index)
    
    return location

print(get_one_bits(37))