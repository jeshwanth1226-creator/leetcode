class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={0:1}
        count=0
        curr_sum=0
        for i in nums:
            curr_sum+=i
            rem=curr_sum % k
            if rem in freq:
                count+=freq.get(rem)
            freq[rem]=freq.get(rem,0)+1
        return count

        

        