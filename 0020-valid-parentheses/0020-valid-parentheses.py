class Solution(object):
    def isValid(self, s):
        O="([{"
        C=")]}"
        stack=[]
        for i in s:
            if i in O:
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if O.index(top)!=C.index(i):
                    return False
        return len(stack)==0