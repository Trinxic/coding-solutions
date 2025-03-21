# @leet start

matching: dict[str:str] = {")": "(", "]": "[", "}": "{"}


class Solution:
    def isValid(self, s: str) -> bool:
        queue: list[str] = []
        for brack in s:
            if brack in {"(", "[", "{"}:
                queue.append(brack)
                continue
            try:
                if queue.pop() != matching[brack]:
                    return False
            except Exception:
                return False
        return len(queue) == 0


# @leet end

