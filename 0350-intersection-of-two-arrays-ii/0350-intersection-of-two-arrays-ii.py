class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=list()
        for ch in set(nums1):
            if ch in set(nums2):
                for i in range(min(nums1.count(ch),nums2.count(ch))):
                    l.append(ch)
        return l

        