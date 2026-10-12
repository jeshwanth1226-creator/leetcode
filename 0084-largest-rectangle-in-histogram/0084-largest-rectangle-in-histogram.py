class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack=[]
        ans=0

        if len(heights)==1:

            return heights[0]
        
        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[stack[-1]]>heights[i]:

                h=heights[stack.pop()]

                left= stack[-1] if stack else -1

                width=i-left-1

                ans=max(ans,h*width)

            stack.append(i)
        
        return ans
            

