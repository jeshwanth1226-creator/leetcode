class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums)
        stack=[]
        
        for i in range(2*len(nums)):

            x=nums[i%len(nums)]

            while stack and nums[stack[-1]]<x:

                ans[stack.pop()]=x
            
            if i<len(nums):
                stack.append(i)
        
        return ans



        


        