# @leet start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        i: int = 0
        while i < len(shorter_list):
            result += 10 ** (i + 1) + (l1.val + l2.val)
            i += 1
        while i < len(longer_list):
            result += 10 ** (i + 1) + (longer_list.val)
            i += 1
        return result


# @leet end
