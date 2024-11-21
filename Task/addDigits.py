class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num


def test_unit():
    solution = Solution()
    print(solution.addDigits(4))
    print(solution.addDigits(11))
    print(solution.addDigits(14))
    print(solution.addDigits(38))
    print(solution.addDigits(169358))
