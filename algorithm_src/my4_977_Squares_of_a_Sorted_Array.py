"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        neg = []
        pos = []
        max = len(nums)
        for i in nums:
            if i >= 0:
                pos.append(i * i)
            else:
                neg.append(i * i)
        neg.reverse()
        indp = 0
        indn = 0
        arr = []
        if neg == []: return pos
        if pos == []: return neg
        for i in range(max):
            if pos[indp] < neg[indn]:
                arr.append(pos[indp])
                indp += 1
                if (indp >= len(pos)):
                    arr += neg[indn:]
                    break
            else:
                arr.append(neg[indn])
                indn += 1
                if (indn >= len(neg)):
                    arr += pos[indp:]
                    break
        return arr