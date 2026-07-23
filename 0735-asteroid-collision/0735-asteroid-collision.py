class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids:
            alive=True
            while alive and stack and i<0 and stack[-1]>0 :
                if stack[-1]<abs(i):
                    stack.pop()
                elif stack[-1]==abs(i):
                    stack.pop()
                    alive=False
                else:
                    alive=False
            if alive:
                stack.append(i)
        return stack

                





                