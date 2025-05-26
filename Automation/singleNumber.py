class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for n in nums:
            if n in arr:
                arr.remove(n)
            else:
                arr.append(n)

        print(arr[0])
        return arr[0]


def test_unit():
    solution = Solution()
    solution.singleNumber([1, 2, 3, 2, 3])
