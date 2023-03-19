import pytest
from ..algorithm_src.my2_278_First_Bad_Version import Solution, tver
from ..tools.time_limit import time_limit


@pytest.fixture()
def prep():
    yield Solution()


@pytest.mark.parametrize('vermax', [4, 5, 10, 15])
@time_limit(2)
def test(prep, vermax):
    global tver
    assert prep.firstBadVersion(vermax) == tver

