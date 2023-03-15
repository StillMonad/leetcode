"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        ind = int(len(nums) / 2)
        step = max(int(len(nums) / 4), 1)

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        while True:
            if nums[ind] == target:
                return ind
            if (ind > 0) and (nums[ind] > target) and (nums[ind - 1] < target):
                return ind
            if target > nums[ind]:
                ind += step
            else:
                ind -= step
            step = max(int(step / 2), 1)

