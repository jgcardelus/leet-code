class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        slow = self.sortList(head)
        fast = self.sortList(mid)

        return self.mergeLists(slow, fast)

    def mergeLists(self, slow, fast):
        anchor = ListNode(0, None)

        head = anchor
        while slow and fast:
            if slow.val < fast.val:
                head.next = slow
                head = slow
                slow = slow.next
            else:
                head.next = fast
                head = fast
                fast = fast.next

        head.next = slow or fast

        return anchor.next

solver = Solution()

test = [3,4,1]
linked_list = None
for i in reversed(test):
    if linked_list is None:
        linked_list = ListNode(i, None)
    else:
        linked_list = ListNode(i, linked_list)


def to_string(head):
    if not head:
        return ""

    acc = str(head.val)
    if head.next:
        acc += " -> " + to_string(head.next)

    return acc


head = solver.sortList(linked_list)
print(to_string(head))
