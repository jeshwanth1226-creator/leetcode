class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        first=len(nums)

        # Lower bound
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                first=mid
                right = mid-1
            else:
                left = mid + 1

        # Target doesn't exist
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        left = 0
        right = len(nums)-1
        last=len(nums)

        # Upper bound
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                last = mid
                right=mid-1
            else:
                left = mid + 1

        return [first, last - 1]

        