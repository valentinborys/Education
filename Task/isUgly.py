class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n % 2 == 0 or n % 3 == 0 or n % 5:
            return False
        else:
            return True


def test_unit():
    solution = Solution()
    solution.isUgly(2)