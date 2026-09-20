class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # kadanes min_sum ,max_sum
        curr_min=min_sum=nums[0]
        curr_max=max_sum=nums[0]

        for i in range(1,len(nums)):

            curr_min=min(nums[i],curr_min+nums[i])
            min_sum=min(min_sum,curr_min)

            curr_max=max(nums[i],curr_max+nums[i])
            max_sum=max(max_sum,curr_max)

        # if all intergers are -ve in nums then max sum is also a -ve number

        if max_sum<0:

            return max_sum
            
        #wrapping sum max=total-kadanes min sum
        wrapping_sum=sum(nums)-min_sum

        return max(wrapping_sum,max_sum)

        
        
        