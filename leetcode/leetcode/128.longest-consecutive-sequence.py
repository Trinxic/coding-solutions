# @leet start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set: set[int] = set(nums)
        longest: int = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                i = 1
                while num + i in nums_set:
                    i += 1
                longest = max(i, longest)
        return longest
# @leet end
