# @leet start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        prod: int = 1
        zero_found: bool = False
        zero_ind: int = -1
        for i, num in enumerate(nums):
            if num == 0:
                if zero_found:
                    return len_nums * [0]
                zero_found = True
                zero_ind = i
            else:
                prod *= num

        if zero_ind != -1:
            return zero_ind * [0] + [prod] + (len_nums - zero_ind - 1) * [0]

        return [prod//num for num in nums]
# @leet end
