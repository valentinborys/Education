class TestSolution(object):
    @staticmethod
    def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        x = (n & (n - 1)) == 0
        print(x)
        return x


def test_unit():
    solution = TestSolution()
    solution.isPowerOfTwo(8)
    solution.isPowerOfTwo(3)
    solution.isPowerOfTwo(12)
    solution.isPowerOfTwo(56)
    solution.isPowerOfTwo(16)
    solution.isPowerOfTwo(1024)
