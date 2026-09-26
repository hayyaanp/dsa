def add_binary(A, B):
    C = [0, 0, 0]

    carry = 0
    for i in range(len(A)-1, -1, -1):
        C[i + 1] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) // 2

    C[0] = carry
    return C


print(add_binary([0, 1], [0, 1])) # C = [0, 1, 0]