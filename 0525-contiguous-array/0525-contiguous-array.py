class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={0:-1}
        max_len=0
        curr_sum=0
        for i,num in enumerate(nums):
            if num==0:
                curr_sum-=1
            else:
                curr_sum+=1
            if curr_sum in seen:
                max_len=max(max_len,i-seen[curr_sum])
            else:
                seen[curr_sum]=i
        return max_len
        