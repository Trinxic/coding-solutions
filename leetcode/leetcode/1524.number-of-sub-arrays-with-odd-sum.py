# @leet start
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        arr_len: int = 0  # length of the array (calculated after first `for` loop)
        odd_sum_count: int = 0  # to be `return`ed

        # number of subarrays which start at 0th index (0, 0,1, 0,1,2, etc.)
        # with an odd amount of 'odd's in them
        #     -> odd number of 'odd's means sum is 'odd'
        odd_subarr_from_zero: int = 0
        odd_number_of_odds: bool = False  # 'even' before finding any 'odd's

        for num in arr:
            arr_len += 1
            # flip-flop when encountering an odd
            odd_number_of_odds = (num % 2 != 0) ^ odd_number_of_odds
            # 'even' when sum is 'odd' means sum is still 'odd'
            if odd_number_of_odds:  #
                odd_subarr_from_zero += 1

        for i, num in enumerate(arr):
            # reduce the memory that `odd_sum_count` uses
            odd_sum_count = (odd_sum_count + odd_subarr_from_zero) % (10**9 + 7)
            # if num is 'even', the sum will be the same as whatever the prev
            # parity was -> add the same amount of 'odd'-sums to the total.
            # if num is 'odd', reevaluate -> amount of 'odd' subarrays left
            # given the amount of the array that is remaining.
            if num % 2 != 0:
                odd_subarr_from_zero = arr_len - i - odd_subarr_from_zero

        return odd_sum_count


# @leet end
