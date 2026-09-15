from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left=0
        output=[]
        dq=deque()

        for right in range(len(nums)):

            while dq and nums[dq[-1]]<=nums[right]:

                dq.pop()

            dq.append(right)

            if dq[0]<left:

                dq.popleft()

            if right-left+1==k:

                output.append(nums[dq[0]])
                left+=1
            
        return output


            




        