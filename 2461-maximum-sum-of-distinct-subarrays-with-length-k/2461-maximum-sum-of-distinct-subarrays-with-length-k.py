class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={}
        window=0
        max_sum=0
        for i in nums[:k]:
            window+=i
            freq[i]=freq.get(i,0)+1
        max_sum= window if len(freq)==k else 0

        for right in range(k,len(nums)):

            window+=nums[right]
            freq[nums[right]]=freq.get(nums[right],0)+1

            old=right-k
            window-=nums[old]
            freq[nums[old]] -=1

            if freq[nums[old]]==0:
                del freq[nums[old]]
            
            if len(freq)==k:
                max_sum=max(max_sum,window)
        return max_sum


