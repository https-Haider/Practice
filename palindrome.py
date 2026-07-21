def palindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return "Not a palindrome"
        if s[l] == s[r]:
            l += 1
            r -= 1  
    return "Is a palindrome"

print(palindrome("hello"))
print(palindrome("radar"))
