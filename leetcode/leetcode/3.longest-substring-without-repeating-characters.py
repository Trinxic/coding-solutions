# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current: int = 0
        longest: int = 0
        recent_repeat: int = 0
        last_occurence: dict[str:int] = {}

        for i, letter in enumerate(s):
            # will ignore reoccurring letters if they happened before the recent
            # repeat since a new substring is being recorded where said letter
            # hasn't occurred yet
            if letter in last_occurence and last_occurence[letter] >= recent_repeat:
                recent_repeat = last_occurence[letter]
                longest = max(current, longest)
                current = i - last_occurence[letter]
            else:
                current += 1
            last_occurence[letter] = i

        return max(longest, current)
# @leet end
