class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0 
        right=len(nums)-1

        #k can be grater than len(nums)
        k=k%len(nums)

        #Reversing whole array
        while left<=right:

            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        
        #Reversign the first k digits
        left=0
        right=k-1

        while left<=right:

            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        
         #Reversign the remaining digits
        left=k
        right=len(nums)-1

        while left<=right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        
        return nums



            

        