def isPalindrome(str1):
    if len(str1) < 1:
        return True
    return str1[0] == str1[-1] and isPalindrome(str1[1:-1])

print(isPalindrome("owoaeeaowo"))