# @leet start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sequences: dict[int: list[int]] = {}
        longest: int = 0
        seq_min: int = 0
        seq_max: int = 1
        for i, num in enumerate(nums):
            if num in sequences:
                continue  # ignore duplicates

            lower = upper = num
            sequences[num] = [lower, upper]  # num<-num->num

            if num - 1 in sequences:
                lower = sequences[num - 1][seq_min]
                upper = max(sequences[sequences[num - 1][seq_min]][seq_max], upper)

            if num + 1 in sequences:
                lower = min(sequences[sequences[num + 1][seq_max]][seq_min], lower)
                upper = sequences[num + 1][seq_max]

            # ...<-lower->upper  and  lower<-upper->...
            sequences[lower][seq_max], sequences[upper][seq_min] = upper, lower
            sequences[num] = [lower, upper]  # lower<-num->upper
            longest = max(longest, upper - lower + 1)

        return longest
# @leet end
