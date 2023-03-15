"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. 
You should minimize the number of calls to the API.
"""


import math
from copy import copy


tver = 4


def isBadVersion(version: int) -> bool:
    return version >= tver


class Solution:
    def firstBadVersion(self, n: int) -> int:
        ind = max(int(n / 2), 1)
        step = max(int(n / 4), 1)
        pr_res = False
        global tver
        for _ in range(int(math.sqrt(n) + 2)):
            res = not isBadVersion(ind)
            if pr_res and not res and step == 1:
                return ind
            if res:
                ind += step
            else:
                ind -= step
            step = max(int(step / 2), 1)
            pr_res = copy(res)
