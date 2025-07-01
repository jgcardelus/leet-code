# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        def dfs_and_pop(head, n):
            if head is None:
                return head, 1
            if head.next is None:
                if n == 1:
                    return None, 1
                else:
                    return head, 1

            prev, depth = dfs_and_pop(head.next, n)
            current_depth = depth + 1

            if current_depth == n:
                return prev, current_depth
            else:
                head.next = prev
                return head, current_depth

        head, _depth = dfs_and_pop(head, n)
        return head
