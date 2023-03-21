"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combs = []

        def combinator(start, maximum, length, ret):
            nonlocal combs
            if length == 0:
                combs += [ret]
                return
            for i in range(start, maximum + 1):
                combinator(i + 1, maximum, length - 1, ret + [i])

        combinator(1, n, k, [])
        return combs
