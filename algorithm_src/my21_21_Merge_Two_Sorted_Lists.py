"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h1.val < h2.val:
            return ListNode(h1.val, self.mergeTwoLists(h1.next, h2))
        else:
            return ListNode(h2.val, self.mergeTwoLists(h1, h2.next))
