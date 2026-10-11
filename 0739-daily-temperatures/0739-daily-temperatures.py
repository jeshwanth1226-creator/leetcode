class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        ans=[0]*len(temperatures)

        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]]<temperatures[i]:
                ans[stack.pop()]=i-stack[-1]
            
            stack.append(i)
        
        return ans

        