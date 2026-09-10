class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=set()
        for i,target in enumerate(nums):
            seen={}
            for j,digit in enumerate(nums[i+1:]):
                number=-(target+digit)
                if number in seen:
                    a.add(tuple(sorted([target,digit,number])))
                seen[digit]=j
        return [list(x) for x in a]
        