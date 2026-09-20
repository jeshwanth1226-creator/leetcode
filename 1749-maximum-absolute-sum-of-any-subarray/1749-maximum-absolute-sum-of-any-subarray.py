class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max=max_sum=nums[0]
        curr_min=min_sum=nums[0]

        for i in range(1,len(nums)):

            curr_max=max(nums[i],curr_max+nums[i])
            max_sum=max(max_sum,curr_max)

            curr_min=min(nums[i],curr_min+nums[i])
            min_sum=min(min_sum,curr_min)

        return max(max_sum,abs(min_sum))