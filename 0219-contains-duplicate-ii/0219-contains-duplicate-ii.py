class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen={}
        for j in range(len(nums)):
            if nums[j] in seen and abs(seen[nums[j]]-j)<=k:
                return True
            seen[nums[j]]=j
        return False

        