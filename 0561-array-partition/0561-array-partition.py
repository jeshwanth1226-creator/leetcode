class Solution(object):
    def arrayPairSum(self, nums):
        n=len(nums)
        nums.sort() 
        
        add=0
        for k in range(0,n,2):
            add+=nums[k]
        return add
            