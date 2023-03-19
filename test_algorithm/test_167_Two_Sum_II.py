import pytest
from ..tools.time_limit import time_limit
from ..algorithm_src.my8_167_Two_Sum_II import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (([2, 7, 11, 15], 9), [1, 2]),
    (([2, 3, 4], 6), [1, 3]),
    (([-1, 0], -1), [1, 2]),
]


@pytest.mark.parametrize('case', cases)
@time_limit(2)
def test(prep, case):
    assert prep.twoSum(*case[0]) == case[1]
