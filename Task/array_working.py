class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_a = ''.join(map(str, digits))
        y = str(int(str_a) + 1)
        x = list(map(int, y))
        return x


def test_unit():
    unit_test = Solution()
    result_1 = unit_test.plusOne([7, 2, 3, 4, 6])
    result_2 = unit_test.plusOne([0])
    result_3 = unit_test.plusOne([2, 0])
    result_4 = unit_test.plusOne([99, 11])

    print(result_1, result_2, result_3, result_4)
