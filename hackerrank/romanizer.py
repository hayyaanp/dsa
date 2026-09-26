def romanizer(nums):
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (8, "VIII"),
        (7, "VII"),
        (6, "VI"),
        (5, "V"),
        (4, "IV"),
        (3, "III"),
        (2, "II"),
        (1, "I")
    ]

    result = []

    for num in nums:
        roman = ""

        for value, symbol in values:
            while num >= value:
                roman += symbol
                num -= value

        result.append(roman)

    return result

print(romanizer([1, 49, 23])) # ["I", "XLIX", "XXIII"]