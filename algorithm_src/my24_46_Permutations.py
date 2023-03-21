"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms = []
        if len(nums) == 0 or len(nums) == 1:
            return nums
        def helper(arr, depth):

a = Solution()
print(a.permute([1, 2, 3]))
