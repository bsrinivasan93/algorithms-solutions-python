from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dict = defaultdict(list)
    for str in strs:
        charCount = [0] * 26
        for c in str:
            charCount[ord(c) - ord('a')] += 1
        
        dict[tuple(charCount)].append(str)

    return dict.values()


# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["a"]))