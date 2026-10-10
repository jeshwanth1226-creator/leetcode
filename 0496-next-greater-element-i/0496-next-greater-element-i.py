class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        pos = {}
        for i in range(len(nums1)):
            pos[nums1[i]] = i

        s=set(nums1)
        stack=[]
        ans=[-1]*len(nums1)

        for i,x in enumerate(nums2):

                while stack and nums2[stack[-1]]<x:
                    
                    ans[pos[nums2[stack.pop()]]]=x
                
                if x in s:
                    stack.append(i)
        
        return ans


        