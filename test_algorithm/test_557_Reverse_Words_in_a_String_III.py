import pytest
from ..tools.time_limit import time_limit
from ..algorithm_src.my10_557_Reverse_Words_in_a_String_III import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD")
]


@pytest.mark.parametrize('case', cases)
@time_limit(2)
def test(prep, case):
    assert prep.reverseWords(case[0]) == case[1]
