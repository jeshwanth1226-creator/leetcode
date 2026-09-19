class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_min=curr_max=max_prod=nums[0]

        for i in range(1,len(nums)):

            old_max,old_min=curr_max,curr_min

            curr_max=max(nums[i],old_max*nums[i],old_min*nums[i])

            curr_min=min(nums[i],old_max*nums[i],old_min*nums[i])
            
            max_prod=max(curr_max,max_prod)

        return max_prod
        