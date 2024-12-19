# Definition for singly-linked list.
from typing import Optional

# Reverse single linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        # Recursion
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(headf.next)
            head.next.next = head
        head.next = None
        return newHead