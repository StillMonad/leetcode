import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm_src.my6_189_Rotate_Array import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
    (([-1, -100, 3, 99], 2), [3, 99, -1, -100]),
    (([1, 2], 3), [2, 1])
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(2)
def test(prep, case):
    nums = case[0][0]
    prep.rotate(nums, case[0][1])
    assert nums == case[1]
