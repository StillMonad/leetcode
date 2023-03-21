import pytest
from ..tools.time_limit import time_limit
from ..algorithm_src.my23_77_Combinations import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ((4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    ((1, 1), [[1]]),
]


@pytest.mark.parametrize('case', cases)
@time_limit(2)
def test(prep, case):
    res = prep.combine(*case[0])
    res = set((tuple(i) for i in res))
    intended = set((tuple(i) for i in case[1]))
    assert res == intended
