import pytest
from ..algorithm.my2_278_First_Bad_Version import Solution, tver
from ..tools.limit_exec_time import limit_exec_time


@pytest.fixture()
def prep():
    yield Solution()


@pytest.mark.parametrize('vermax', [4, 5, 10, 15])
@limit_exec_time(2)
def test(prep, vermax):
    global tver
    assert prep.firstBadVersion(vermax) == tver

