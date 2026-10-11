class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        pos={}
        for i,x in enumerate(nums1):
            pos[x]=i
        s=set(nums1)
        ans=[-1]*len(nums1)

        for i in range(len(nums2)):

            if nums2[i] in s:

                j=i+1

                while j<len(nums2):

                    if nums2[i]<nums2[j]:
                        ans[pos[nums2[i]]]=nums2[j]
                        break
                    j+=1

        return ans
        