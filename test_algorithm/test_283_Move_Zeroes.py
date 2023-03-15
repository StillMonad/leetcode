import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm.my7_283_Move_Zeroes import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0])
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(2)
def test(prep, case):
    nums = case[0]
    prep.moveZeroes(nums)
    assert nums == case[1]