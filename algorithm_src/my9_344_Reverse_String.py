"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        # s.reverse() - probably not O(1) memory
        # s[:] = s[::-1] - probably not O(1) memory
        for i in range(0, int(len(s) / 2)):
            s[i], s[-i - 1] = s[-i - 1], s[i]