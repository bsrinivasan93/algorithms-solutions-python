def isPalindrome(inputStr):
    newStr = ''
    for c in inputStr:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

def isPalindrome2Pointer(inputStr):
    l = 0
    r = len(inputStr)-1

    while l<r:
        while not alphaNum(inputStr[l]):
            l += 1
        while not alphaNum(inputStr[r]):
            r -= 1
        if inputStr[l].lower() != inputStr[r].lower():
             return False
        l, r = l+1, r-1
        
    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
    (ord('a') <= ord(c) <= ord('z')) or
    (ord('0') <= ord(c) <= ord('9')))

s = "A man, a plan, a canal: Panama"
print(isPalindrome2Pointer(s))