class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        addn=0
        min_count=float('inf')

        if target>sum(nums):
            return 0

        for right in range(len(nums)):
            addn+=nums[right] 

            while addn>=target:
                
                min_count=min(min_count,right-left+1)

                addn-=nums[left]
                left+=1
            
        return 0 if min_count==float('inf') else min_count
            
            
        