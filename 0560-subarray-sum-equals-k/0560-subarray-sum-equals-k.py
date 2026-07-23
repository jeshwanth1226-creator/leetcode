class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={0:1}
        curr_sum=0
        count=0
        for i in nums:
            curr_sum+=i
            if curr_sum - k in freq:
                count+=freq.get(curr_sum-k)
            freq[curr_sum]=freq.get(curr_sum,0)+1
        return count

        
