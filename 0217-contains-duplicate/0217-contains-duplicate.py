class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]==2:
                return True
        return False
        