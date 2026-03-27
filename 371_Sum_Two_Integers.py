def getSum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    max_int = 0x7FFFFFFF

    while b:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
    return a if a <=  max_int else ~(a ^ mask)

print(getSum(-1,1))