"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""


import math


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        curr = int(len(nums) / 2)
        step = max(int(len(nums) / 4), 1)
        count = math.sqrt(len(nums)) + 1
        while count > 0:
            if target == nums[curr]:
                return curr
            if target < nums[curr]:
                curr -= step
            else:
                curr += step
            step = step = max(int(step / 2), 1)
            count -= 1
        return -1
