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
        list3 = [x for x in list1] + [x for x in list2]
        print(type(list3))
        return type(list3)

def test_unit():
    solution = Solution()
    solution.mergeTwoLists([5, 0], [2, 3])