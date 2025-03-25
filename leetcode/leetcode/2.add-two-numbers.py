# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum: int = 0  # 1's column of the l1+l2 sum
        overflow: int = 0  # 10's column of the sum
        overflow, sum = divmod(l1.val + l2.val, 10)  # assumes both lists aren't empty
        l1, l2 = l1.next, l2.next
        result: ListNode = ListNode(sum)  # head of the resulting list
        ptr: ListNode = result  # point to last node in the list

        while l1 is not None and l2 is not None:
            overflow, sum = divmod(l1.val + l2.val + overflow, 10)
            ptr.next = ListNode(sum)
            l1, l2, ptr = l1.next, l2.next, ptr.next

        if l1 is not None:  # l1 is longer than l2
            while l1 is not None:
                overflow, sum = divmod(l1.val + overflow, 10)
                ptr.next = ListNode(sum)
                l1, ptr = l1.next, ptr.next
        # technically, `if` could be used, but this is slightly better readability
        elif l2 is not None:  # l2 is longer than l1
            while l2 is not None:
                overflow, sum = divmod(l2.val + overflow, 10)
                ptr.next = ListNode(sum)
                l2, ptr = l2.next, ptr.next

        if overflow != 0:  # same as `overflow == 1`
            ptr.next = ListNode(overflow)  # should be same as `ListNode(1)`

        return result


# @leet end
