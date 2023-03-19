import pytest
from ..tools.time_limit import time_limit
from ..algorithm_src.my9_344_Reverse_String import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
]


@pytest.mark.parametrize('case', cases)
@time_limit(2)
def test(prep, case):
    prep.reverseString(case[0])
    assert case[0] == case[1]
