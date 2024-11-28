class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        lowercase = set()
        uppercase = set()

        for i in s:
            if i.isupper():
                uppercase.add(i)
            elif i.islower():
                lowercase.add(i)

        common_letters = {char for char in uppercase if char.lower() in lowercase}

        if not common_letters:
            return ''

        return max(common_letters)


def test_unit():
    solution = Solution()
    solution.greatestLetter('hg')
    solution.greatestLetter("lEeTcOdE")
    solution.greatestLetter("arRAzFif")
    solution.greatestLetter("lEeTcOdE")