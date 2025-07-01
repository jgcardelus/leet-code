class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        if head is None:
            return None

        if head.next is None:
            return head

        head_less = ListNode(0, None)
        less = head_less

        head_greater = ListNode(0, None)
        greater = head_greater

        current = head

        while current:
            if current.val < x:
                less.next = current
                less = current

            if current.val >= x:
                greater.next = current
                greater = current

            current = current.next

        greater.next = None
        less.next = head_greater.next
        return head_greater.next
