class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        else:
            return (n - 1) + (n - 2)


def test_unit():
    solution = Solution()
    way_1 = solution.climbStairs(2)
    way_2 = solution.climbStairs(16)
    way_3 = solution.climbStairs(70)

    print(way_1, way_2, way_3)
