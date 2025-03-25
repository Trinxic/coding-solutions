# @leet start

# from typing import Callable
# operations: dict[str : Callable[[int, int], int]] = {
operations = {
    "+": lambda x, y: y + x,
    "-": lambda x, y: y - x,
    "*": lambda x, y: y * x,
    "/": lambda x, y: int(y / x),
}

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                stack[-1] = operations[token](stack.pop(), stack[-1])
        return stack[0]


# @leet end
