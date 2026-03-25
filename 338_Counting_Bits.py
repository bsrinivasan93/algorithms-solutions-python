def numBits(n):
    res = []
    for i in range(0, n+1):
        numOnes = 0
        for j in range(0,31):
            if (1 << j) & i:
                numOnes += 1
        res.append(numOnes)
    return res

def numBitsDP(n):
    res = [0] * (n+1)
    offset = 1
    for i in range(1, n+1):
        if 2 * offset == i:
            offset = i
        res[i] = 1 + res[i - offset]
    return res

print(numBitsDP(2))
print("h")
print("he")