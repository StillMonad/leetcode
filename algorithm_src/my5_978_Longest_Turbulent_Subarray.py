"""
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
"""


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if arr == []:
            return 0
        curr = 0
        ret = 0
        for i in range(len(arr)):
            if ((i > 1) and
                    ((arr[i - 2] < arr[i - 1] > arr[i]) or
                     (arr[i - 2] > arr[i - 1] < arr[i]))):
                curr += 1
            elif (i > 0) and (arr[i - 1] != arr[i]):
                curr = 2
            else:
                curr = 1
            ret = max(ret, curr)
        return ret