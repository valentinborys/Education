class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_elements = "!@#$%^&*()-+"

        if len(password) < 8 or len(password) > 100:
            return False

        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False

            char = password[i]

            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_elements:
                has_special = True

        last_char = password[-1]
        if last_char.isupper():
            has_upper = True
        elif last_char.islower():
            has_lower = True
        elif last_char.isdigit():
            has_digit = True
        elif last_char in special_elements:
            has_special = True

        return all([has_upper, has_lower, has_digit, has_special])


def test_unit():
    solution = Solution()
    solution = Solution()
    solution.strongPasswordCheckerII("XrVIVr-L)CtyZ7xyo!TiHr859lCIHJ$CYHnCQ$kVafJ-15lKjkXLoW5zQnWa3jlGjH9+QKF&^Jvy1$WajBF9VL3^2Okns63LvMZX")