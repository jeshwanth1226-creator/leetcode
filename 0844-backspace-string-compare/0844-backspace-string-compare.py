class Solution(object):
    def backspaceCompare(self, s, t):
        stack1,stack2=[],[]
        for i in s:
            if i!='#':
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
        s1=''.join(stack1)
        for i in t:
            if i!='#':
                stack2.append(i)
            else:
                if stack2:
                    stack2.pop()
        s2=''.join(stack2)
        return s1 == s2
            
        
                

                
