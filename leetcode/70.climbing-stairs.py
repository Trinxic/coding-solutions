# @leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        result: int = 1
        prev: int = 1
        for _ in range(1, n + 1):
            result, prev = result + prev, result
        return prev
# @leet end
