class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max_ones=0
        for right in range(len(nums)):
            if nums[right]==1:
                count+=1
                max_ones=max(max_ones,count)
            else:
                count=0
        return max_ones
        
        