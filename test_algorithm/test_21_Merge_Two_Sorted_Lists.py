import pytest
from ..algorithm_src.my21_21_Merge_Two_Sorted_Lists import ListNode, Solution
from ..tools.time_limit import time_limit
from ..tools.time_measure import time_measure


@pytest.fixture()
def prep():
    yield Solution()


cases = [
    ((ListNode.create_from([1, 2, 4]), ListNode.create_from([1, 3, 4])),
     ListNode.create_from([1, 1, 2, 3, 4, 4])),
    ((ListNode.create_from([1, 2, 3, 4]), ListNode.create_from([5, 6, 7, 8])),
     ListNode.create_from([1, 2, 3, 4, 5, 6, 7, 8])),
]


@pytest.mark.parametrize('case', cases)
@time_measure
@time_limit(2)
def test(prep, case):
    assert (r := prep.mergeTwoLists(*case[0])) == case[1], \
        f"\n== FAILED ==\n\tRESULT:\n\t\t{str(r)}\n\tEXPECTED:\n\t\t{str(case[1])}"
