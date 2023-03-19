import pytest
from ..tools.time_limit import time_limit
from ..algorithm_src.my4_977_Squares_of_a_Sorted_Array import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ([1], [1])
]


@pytest.mark.parametrize('case', cases)
@time_limit(2)
def test(prep, case):
    assert prep.sortedSquares(case[0]) == case[1], f"Input: {case[0]}"
