
def palindrome(name, left, right):
        if left >= right:
            return True # after it is overlap at the center then it is palindrome
        if name[left] != name[right]:
            return False
        return palindrome(name, left + 1, right - 1)
name = "madam"
print(palindrome(name, 0, len(name) - 1 ))


# def isPalindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
    
# print(isPalindrome("dad"))