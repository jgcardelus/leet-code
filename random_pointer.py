class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        hash = {None:None}
        cur = head

        while cur:
            hash[cur] = Node(cur.val, None, None)
            cur = cur.next

        cur = head

        while cur:
            copy = hash[cur]
            copy.next = hash[cur.next]
            copy.random = hash[cur.random]
            cur = cur.next

        return hash[head]
