class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix=0
        rem={0:1}
        count=0

        for i in range(len(nums)):
            
            prefix+=nums[i]
            r=prefix%k

            if r in rem:
                count+=rem[r]
                rem[r]+=1
            else:
                rem[r]=1
        
        return count

        