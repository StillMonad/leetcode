import pytest
from ..tools.time_limit import time_limit
from ..algorithm_src.my13_3_Longest_Substring_Without_Repeating_Characters import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]


@pytest.mark.parametrize('case', cases)
@time_limit(0.3)
def test(prep, case):
    assert prep.lengthOfLongestSubstring(case[0]) == case[1]
