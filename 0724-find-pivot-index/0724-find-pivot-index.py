class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum=[0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1]+num)
        
        for i in range(len(nums)):
            left_sum=prefix_sum[i]
            right_sum=(prefix_sum[-1]-prefix_sum[i+1])
            if left_sum==right_sum:
                return i
        return -1

        