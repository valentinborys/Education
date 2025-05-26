class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index = []
        for i, num in enumerate(nums):
            if target - num == 0:
                index.append(index[num])
        print(index)


def test_unit():
    solution = Solution()
    solution.twoSum([2, 7, 11, 15], 2)