class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stacks=[]
        stackt=[]

        for i in s:
            if i!='#':
                stacks.append(i)
            else:
                if stacks:
                    stacks.pop()
        
        for i in t:
            if  i!='#':
                stackt.append(i)
            else:
                if stackt:
                    stackt.pop()            
        if stacks==stackt:
            return True
        
        return False
        
            
        