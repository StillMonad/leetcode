"""
Given a string s, find the length of the longest
substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        keys = set(s)
        a = a.fromkeys(keys)
        substr = ""
        max = ""
        i = 0
        while i < len(s):
            if a[s[i]] != None:
                substr = ""
                i = a[s[i]] + 1
                a = {}.fromkeys(keys)
            substr += s[i]
            a[s[i]] = i
            max = substr if len(substr) > len(max) else max
            i += 1
        return len(max)
