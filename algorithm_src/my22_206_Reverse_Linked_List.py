"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from collections import deque
from typing import Optional


# Definition for singly-linked list (for testing).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_from(list):
        if list == []: return None
        return ListNode(list[0], ListNode.create_from(list[1:]))

    def __eq__(self, other):
        if type(other) == type(self) and self.val == other.val:
            return True and self.next.__eq__(other.next)
        return False

    def __str__(self):
        return str(str(self.val) + ' ' + ('' if self.next == None else self.next.__str__()))


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        queue = deque()
        queue.append(None)
        if head == None:
            return head

        while True:
            queue.append(ListNode(head.val, head.next))
            elt = queue.popleft()
            queue[0].next = elt
            head = head.next
            if head == None:
                elt = queue.popleft()
                return elt
