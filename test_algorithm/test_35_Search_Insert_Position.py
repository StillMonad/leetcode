import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm.my3_35_Search_Insert_Position import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (([1, 3, 5, 6], 5), 2),
    (([1, 3, 5, 6], 2), 1),
    (([1, 3, 5, 6], 7), 4),
    (([1, 3, 5, 6], 2), 1),
    (([1, 2, 4, 6, 8, 9, 10], 10), 6),
    (([1, 4, 6, 7, 8, 9], 6), 2),
    (([1], 1), 0)
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(2)
def test(prep, case):
    assert prep.searchInsert(*case[0]) == case[1]
