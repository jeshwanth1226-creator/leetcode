class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #original kadanes max_sum

        curr_sum=orig_max_sum=nums[0]

        for i in range(1,len(nums)):

            curr_sum=max(nums[i],curr_sum+nums[i])
            orig_max_sum=max(orig_max_sum,curr_sum)

        #reversing signs & kadanes max_sum

        for i in range(len(nums)):

            nums[i]=-nums[i]

        curr_sum=max_sum=nums[0]

        for i in range(1,len(nums)):

            curr_sum=max(nums[i],curr_sum+nums[i])
            max_sum=max(max_sum,curr_sum)

        return max(orig_max_sum,max_sum)

