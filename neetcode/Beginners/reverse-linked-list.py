# Definition for singly-linked list.
from typing import List, Optional

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
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

# Designing singly linked list:

# Need ListNode class

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # Dummy node, useful for edgecases (emptty list)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) # Need to create this node first
        new_node.next = self.head
        self.head = new_node

        # If list started empty, self.head.next = null
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # Two cases, list is empty therefore tail = head
        
        new_node = ListNode(val)
        if not self.head.next:
            self.tail.next = new_node
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        # curr = self.head.next
        curr = self.head
        i = 0
        while i < index and curr: # < so it gets the index before the one we want, curr prevents out of bounds
            i+=1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail: # Handle removal of tail
                self.tail = curr

            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        list = []
        curr = self.head.next
        while curr:
            list.append(curr.val)
            curr = curr.next

        return list
            
