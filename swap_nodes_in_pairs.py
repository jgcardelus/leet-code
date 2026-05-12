# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        anchor = ListNode(0, head)

        def swap_and_move(anchor, head):
            if not head or not head.next:
                return

            # Swap adjancent
            next = head.next
            head.next = next.next
            next.next = head
            anchor.next = next

            # Move to next pair
            swap_and_move(head, head.next)

        swap_and_move(anchor, head)
        return anchor.next
