import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm_src.my1_704_Binary_Search import Solution

@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1)
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(2)
def test(prep, case):
    assert prep.search(*case[0]) == case[1]

