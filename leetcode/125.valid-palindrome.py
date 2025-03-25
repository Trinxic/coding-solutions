# @leet start
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([character.lower() for character in s if character.isalnum()])
        s_len: int = len(s)

        for i in range((s_len + 1) // 2):
            if s[i] != s[s_len - i - 1]:
                return False
        return True
"""

### Optimal solution (instead of recreating the string):
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1

        return True
# @leet end
