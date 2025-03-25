# @leet start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sums: dict[int:int] = {}  # {target - num: index of num}
        for i, num in enumerate(nums):
            if (target - num) in sums:
                return [sums[target - num], i]
            else:
                sums[num] = i
        return None


# @leet end
