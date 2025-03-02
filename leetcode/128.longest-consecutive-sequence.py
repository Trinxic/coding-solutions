# @leet start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences: dict[int:int] = {}
        for i, num in enumerate(nums):
            if num in sequences:
                continue  # ignore duplicates
            sequences[num] = num
            if num - 1 in sequences:
                if num > sequences[sequences[num - 1]]:
                    sequences[sequences[num - 1]] = num
                    sequences[num] = sequences[num - 1]
            if num + 1 in sequences:
                val = sequences[num]
                if val < sequences[sequences[num + 1]]:
                    sequences[sequences[num + 1]] = val
                    sequences[val] = sequences[num + 1]
        return sequences


# @leet end

"""

"""

