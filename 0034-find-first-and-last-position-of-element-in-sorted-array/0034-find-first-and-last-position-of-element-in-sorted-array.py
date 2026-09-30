class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)

        # Lower bound
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        first = left

        # Target doesn't exist
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        left = 0
        right = len(nums)

        # Upper bound
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return [first, left - 1]

        