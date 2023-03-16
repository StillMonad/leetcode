"""
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes
of the two trees are overlapped while the others are not. You need to merge
the two trees into a new binary tree. The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.
Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, n1, n2) -> Optional[TreeNode]:
        if n1 == None and n2 == None:
            return None
        if n1 == None:
            return n2
        if n2 == None:
            return n1
        n3 = TreeNode(n1.val + n2.val, self.mergeTrees(n1.left, n2.left), self.mergeTrees(n1.right, n2.right))
        return n3


