"""
Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [i for i in nums if i != 0] + [0] * nums.count(0)
