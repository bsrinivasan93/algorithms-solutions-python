def climbStairs(n: int) -> int:
    one, two = 1, 1

    for i in range(0, n-1):
        tmp = one + two
        one, two = tmp, one
    
    return one

print(climbStairs(5))