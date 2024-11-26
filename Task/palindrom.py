class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = ''.join(ch for ch in s.lower() if ch.isalnum())
        reversed_filtered = filtered[::-1]

        return filtered == reversed_filtered


def test_unit():
    solution = Solution()
    solution.isPalindrome("A man, a plan, a canal: Panama....")

