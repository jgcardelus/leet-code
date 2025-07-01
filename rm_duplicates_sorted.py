# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head.next is None:
            return head

        prehead = ListNode(0, head)
        pin = prehead
        prev = prehead
        current = head

        while current:
            if current.val == prev.val:
                pin.next = current.next
            else:
                if current.next is None:
                    break

                if current.next.val != current.val:
                    pin = current

            prev = current
            current = current.next

        return prehead.next



# [1,2,3,3,4,4,5]
lst = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, None)))))))
solver = Solution()
solution = solver.deleteDuplicates(lst)

next = solution
while next:
    print(next.val, end=", ")
    next = next.next
