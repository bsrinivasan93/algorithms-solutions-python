# https://leetcode.com/problems/top-k-frequent-elements/description/

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freqList = [[] for i in range(0, len(nums)+1)]

    for num in nums:
        count[num] = count.get(num, 0) + 1
    print(count)
    for n, c in count.items():
        freqList[c].append(n)
    print(freqList)

    res = []
    for i in range(len(freqList)-1, 0, -1):
        for n in freqList[i]:
            res.append(n)
            print(f"added {n} to {res}")
            if len(res) == k:
                return res

print(topKFrequent([1,1,1,2,2,3],2))
