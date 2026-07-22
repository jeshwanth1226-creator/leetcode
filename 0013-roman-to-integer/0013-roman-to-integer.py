class Solution(object):
    def romanToInt(self, s):
        nums=list(s)
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        for i in range(len(nums)-1):
            if (d[nums[i]]<d[nums[i+1]]):
                sum+=-d[nums[i]]
            else:
                sum+=d[nums[i]]
    
        sum+=d[nums[-1]]
        return sum
                
        