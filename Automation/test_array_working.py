<<<<<<<< HEAD:Automation/test_array_working.py
import allure
========
from decorators import screenshot_on_failure
>>>>>>>> 5db0e593f0a3ed79eb7bf725ef7098a2c1d5f56f:Automation/array_working.py


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

<<<<<<<< HEAD:Automation/test_array_working.py
@allure.feature('BalancesTest')
@allure.title('Mid correct adjust balance work 3')
@allure.severity(allure.severity_level.CRITICAL)
========
@screenshot_on_failure
>>>>>>>> 5db0e593f0a3ed79eb7bf725ef7098a2c1d5f56f:Automation/array_working.py
def test_unit():
    unit_test = Solution()
    result_1 = unit_test.plusOne([7, 2, 3, 4, 6])
    result_2 = unit_test.plusOne([0])
    result_3 = unit_test.plusOne([2, 0])
    result_4 = unit_test.plusOne([99, 11])

    print(result_1, result_2, result_3, result_4)
