# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 1. Swap
        helper = node.next.val
        node.next.val = node.val
        node.val = helper

        # 2. If next is tail, remove. Else, continue pushing
        if node.next.next is not None:
            self.deleteNode(node.next)
        else:
            node.next = None
