import pytest
from ..tools.time_limit import time_limit
from ..tools.time_measure import time_measure
from ..algorithm_src.my20_994_Rotting_oranges import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ([[2, 1, 1],
      [1, 1, 0],
      [0, 1, 1]], 4,),

    ([[2, 1, 1],
      [0, 1, 1],
      [1, 0, 1]], -1,),

    ([[0, 2]], 0,),

    ([[0]], 0,),

    ([[2, 1, 1],
      [1, 1, 1],
      [0, 1, 2]], 2),
]


@pytest.mark.parametrize('case', cases)
def test(prep, case):
    assert prep.orangesRotting(case[0]) == case[1]
