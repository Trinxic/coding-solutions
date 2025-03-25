# @leet start
class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        # whatever number will replace this at the start
        self.min_val: int = 0  # place holder

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            # append how much lower or higher the new val is to the prev min val
            self.stack.append(val - self.min_val)
            self.min_val = min(val, self.min_val)  # change if new val is lower

    def pop(self) -> None:
        if (popped := self.stack.pop()) < 0:  # `popped` was lower than the prev min
            # subtract a negative => more positive number
            # prev min was `popped`-units above now-popped min|val
            self.min_val -= popped

    def top(self) -> int:
        if (top := self.stack[-1]) < 0:  # top of stack is the lowest
            return self.min_val
        # top of stack was `self.stack[-1]`-units away from min
        return top + self.min_val

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end
