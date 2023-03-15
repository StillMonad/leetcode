import pytest
from ..tools.limit_exec_time import limit_exec_time
from ..algorithm.my5_978_Longest_Turbulent_Subarray import Solution


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ([9, 4, 2, 10, 7, 8, 8, 1, 9], 5),
    ([4, 8, 12, 16], 2),
    ([100], 1),
    ([2, 0, 2, 4, 2, 5, 0, 1, 2, 3], 6),
    ([9, 9], 1),
    ([8, 8, 9, 10, 6, 8, 2, 4, 2, 2, 10, 6, 6, 10, 10, 2, 3, 5, 1, 2, 10, 4, 2, 0, 9, 4, 9, 3, 0, 6, 3, 2, 3, 10, 10, 6,
      4, 6, 4, 4, 2, 5, 1, 4, 1, 1, 9, 8, 9, 5, 3, 5, 5, 4, 5, 5, 6, 5, 3, 3, 7, 2, 0, 10, 9, 7, 7, 3, 5, 1, 0, 9, 6, 3,
      1, 3, 4, 4, 3, 6, 3, 2, 1, 4, 10, 2, 3, 4, 4, 3, 6, 7, 6, 2, 1, 7, 0, 6, 8, 10], 7)
]


@pytest.mark.parametrize('case', cases)
@limit_exec_time(2)
def test(prep, case):
    assert prep.maxTurbulenceSize(case[0]) == case[1], f"Input: {case[0]}"
