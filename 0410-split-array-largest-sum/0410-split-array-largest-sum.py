class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left=max(nums)
        right=sum(nums)

        while left<=right:

            mid=(left+right)//2

            total=0
            parts=1

            for i in nums:
                if total+i<=mid:
                    total+=i
                else:
                    parts+=1
                    total=i
            
            if parts<=k:
                  right=mid-1
            else:
                left=mid+1
        return left

            
                
                

        
        