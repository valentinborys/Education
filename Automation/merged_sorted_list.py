# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        print(sorted(list1 + list2))
        return


def test_unit():
    solution = Solution()
    solution.mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4])

