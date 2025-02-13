from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        head = None
        while head1.val or head2.val:
            if head1.val <= head2.val:
                head.next = head1
                mergedList = self.mergeTwoLists(head1, head2)
            else:
                head.next = head2
                mergedList = self.mergeTwoLists(head1, head2)
        
        return mergedList