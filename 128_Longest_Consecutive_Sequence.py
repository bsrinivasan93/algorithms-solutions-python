def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n - 1) not in numSet:
            length = 1
            while n + length in numSet:
                length += 1
            longest = max(longest, length)

    return longest

print(longestConsecutive([100,4,200,1,3,2]))