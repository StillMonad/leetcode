import pytest
from ..algorithm_src.my22_206_Reverse_Linked_List import ListNode, Solution
from ..tools.time_limit import time_limit
from ..tools.time_measure import time_measure


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    (ListNode.create_from([1, 2, 3, 4, 5]), ListNode.create_from([5, 4, 3, 2, 1])),
    (ListNode.create_from([1, 2]), ListNode.create_from([2, 1])),
    (ListNode.create_from([]), ListNode.create_from([])),
    (ListNode.create_from([1]), ListNode.create_from([1])),
]


@pytest.mark.parametrize('case', cases)
@time_measure
@time_limit(2)
def test(prep, case):
    assert (r := prep.reverseList(case[0])) == case[
        1], f"\n== FAILED ==\n\tRESULT:\n\t\t{str(r)}\n\tEXPECTED:\n\t\t{str(case[1])}"
