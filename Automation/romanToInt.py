class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        array = []
        x = list(s)
        for i in x:
            if i in roman_value:
                array.append(roman_value[i])
        return sum(array)


def test_unit():
    solution = Solution()
    solution.romanToInt('LLX')
    solution.romanToInt('DDDDM')
    solution.romanToInt('MCMXCIV')