class Solution(object):
    def singleNumber(self, nums):
         d=set()
         for i in nums:
            if nums.count(i)==2:
                d.add(i)
            else:
                return i
        

