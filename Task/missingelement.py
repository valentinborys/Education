class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        last_number = nums[-1]
        compare_array = list(range(last_number + 1))
        b = list(set(compare_array) - set(nums))
        if b:
            return b[0]
        else:
            return last_number + 1


def test_unit():
    solution = Solution()
    solution.missingNumber([3,0,1])
    solution.missingNumber([0,1])
    solution.missingNumber([9,6,4,2,3,5,7,0,1])

