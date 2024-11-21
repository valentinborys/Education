class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


def test_unit():
    solution = Solution()
    solution.isPowerOfThree(81)
    solution.isPowerOfThree(27)
    solution.isPowerOfThree(15)


