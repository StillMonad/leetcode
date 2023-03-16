"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
"""
import time
from collections import Counter

"""
not O(n) solution - gets all permutations
class Solution:
    @staticmethod
    def get_permutations(s):
        perms = []

        def permutator(s, depth):
            nonlocal perms
            if len(s) == 1:
                perms = [s]
                return
            if depth == 0:
                perms = list(set(perms))
                return
            for i in range(len(s) - 1):
                ssw = s[:i] + (lambda s: s[1] + s[0])(s[i] + s[i + 1]) + s[i + 2:]
                perms += [ssw]
                permutator(ssw, depth - 1)
        permutator(s, len(s))
        return perms

    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutations = Solution.get_permutations(s1)
        for p in permutations:
            if p in s2:
                return True
        return False
"""
"""
kinda O(n), but slow (~5s for the last test case)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        d1 = {}
        for i in s1:
            d1[i] = s1.count(i)
        for i in range(l2 - l1 + 1):
            d2 = {}
            s3 = s2[i:(i + l1)]
            for i in s3:
                d2[i] = s3.count(i)
            if d1 == d2:
                return True
        return False

"""
""" 
fast (0.01s on the last test case), but example solutions are ~5x faster (0.002s)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        d1 = {}
        d2 = {}

        if l1 > l2:
            return False
        s3 = s2[:l1]
        for i in range(0, l1):
            d1[s1[i]] = s1.count(s1[i])
            d2[s3[i]] = s3.count(s3[i])
        i = 0
        while True:
            if d1 == d2:
                return True
            if i + l1 >= l2:
                break
            d2[s2[i]] -= 1
            if s2[i] in d2 and d2[s2[i]] == 0:
                d2.pop(s2[i])

            if s2[i + l1] in d2:
                d2[s2[i + l1]] += 1
            else:
                d2[s2[i + l1]] = 1

            if i >= l2 - l1:
                break
            i += 1
        return False

"""

# around 0.001s on the last test case (2x faster than examples)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        d1 = {}
        d2 = {}

        if l1 > l2:
            return False

        s3 = s2[:l1]
        s4 = str(set(s1 + s2))
        for i in range(len(s4)):
            d1[s4[i]] = 0
            d2[s4[i]] = 0
        for i in range(0, l1):
            if d1[s1[i]] == 0:
                d1[s1[i]] = s1.count(s1[i])
            if d2[s3[i]] == 0:
                d2[s3[i]] = s3.count(s3[i])
        i = 0
        while True:
            if d1 == d2:
                return True
            if i + l1 >= l2:
                break
            d2[s2[i]] -= 1
            d2[s2[i + l1]] += 1

            if i >= l2:
                break
            i += 1
        return False


"""
code taken from solutions/examples for performance comparsion:

class Solution: 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, matched = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i - w] in cntr:
                if cntr[s2[i - w]] == 0:
                    matched -= 1
                cntr[s2[i - w]] += 1

            if matched == len(cntr):
                return True

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = [0] * 26
        for c in s1:
            mapp[ord(c) - 97] += 1
        i, j, count_chars = 0, 0, len(s1)
        while j < len(s2):
            if mapp[ord(s2[j]) - 97] > 0:
                count_chars -= 1
            mapp[ord(s2[j]) - 97] -= 1
            j += 1
            if count_chars == 0:
                return True
            if j - i == len(s1):
                if mapp[ord(s2[i]) - 97] >= 0:
                    count_chars += 1
                mapp[ord(s2[i]) - 97] += 1
                i += 1

        return False



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)

        s1_len = len(s1)

        for i in range(len(s2) - s1_len + 1):
            if Counter(s2[i:i + s1_len]) == s1_counter:
                return True

        return False

"""