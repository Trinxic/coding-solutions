# @leet start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies: dict[int:int] = {}
        bucket_freq: list[list[int]] = [[] for _ in nums]

        for i, num in enumerate(nums):
            frequencies[num] = frequencies.get(num, 0) + 1
        for num, freq in frequencies.items():
            bucket_freq[freq - 1].append(num)

        ans: list[int] = []
        for lst_nums in reversed(bucket_freq):
            for num in lst_nums:
                ans.append(num)
                if len(ans) == k:
                    return ans
# @leet end

""" -- Library Solution: (pretty sure it's faster (in the Submit results))

from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [num for [num, freq] in Counter(nums).most_common(k)]  # n log k

"""
