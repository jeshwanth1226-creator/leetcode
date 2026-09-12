class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            temp=nums[i]
            j=i-1
            while j>=0 and nums[j]>temp:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=temp
        return nums
        