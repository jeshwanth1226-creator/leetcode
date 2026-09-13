class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        count=0
        max_ones=0

        for right in range(len(nums)):

            if nums[right]==0:
                count+=1

            while count>k:

                if nums[left]==0:
                    count-=1
                
                left+=1
            
            if count<=k:

                max_ones=max(max_ones,right-left+1)
        
        return max_ones




