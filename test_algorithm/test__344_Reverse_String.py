import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm_src.my9_344_Reverse_String import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(2)
def test(prep, case):
    prep.reverseString(case[0])
    assert case[0] == case[1]
