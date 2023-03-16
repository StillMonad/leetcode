import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm_src.my15_733_Flood_Fill import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
(([[1, 1, 1],
   [1, 1, 0],
   [1, 0, 1]], 1, 1, 2), [[2, 2, 2],
                          [2, 2, 0],
                          [2, 0, 1]]),
(([[0, 0, 0],
   [0, 0, 0]], 0, 0, 0), [[0, 0, 0],
                          [0, 0, 0]]),
(([[0, 0, 0],
   [0, 0, 0]], 1, 0, 2), [[2, 2, 2],
                          [2, 2, 2]]),
(([[0, 0, 0],
   [0, 0, 0]], 1, 1, 1), [[1, 1, 1],
                          [1, 1, 1]]),
    (([[0, 1, 0],
       [0, 0, 1]], 1, 1, 1), [[1, 1, 0],
                              [1, 1, 1]]),
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(1)
def test(prep, case):
    assert prep.floodFill(*case[0]) == case[1]
