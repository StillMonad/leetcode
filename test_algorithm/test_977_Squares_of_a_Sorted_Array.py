import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm.my4_977_Squares_of_a_Sorted_Array import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([1], [1])
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(2)
def test(prep, case):
    assert prep.sortedSquares(case[0]) == case[1], f"Input: {case[0]}"
