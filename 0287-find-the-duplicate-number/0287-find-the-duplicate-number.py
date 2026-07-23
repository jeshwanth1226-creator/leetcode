class Solution(object):
    def findDuplicate(self, nums):
        d=set()
        for i in nums:
            if i in d:
                return i
            d.add(i)
        