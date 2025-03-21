# @leet start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        available_nums: list[set[str]] = [set() for _ in range(3 * 9)]
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num.isnumeric():
                    for ind in (i, 9 + j, 18 + i // 3 * 3 + j // 3):
                        try:
                            available_nums[ind].remove(num)
                            return False
                        except KeyError:
                            available_nums[ind].add(num)
        return True
# @leet end

