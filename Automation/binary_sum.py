class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        print(a)
        b = int(b, 2)
        print(b)

        return bin(a + b)[2:]


def test_unit():
    unit = Solution()
    x = unit.addBinary("11", "1")
    print(x)
