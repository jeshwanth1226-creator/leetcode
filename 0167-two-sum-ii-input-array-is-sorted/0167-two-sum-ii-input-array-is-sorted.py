class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i,j in enumerate(numbers):
            res=target-j
            if res in seen:
                return[seen[res]+1,i+1]
            seen[j]=i

        