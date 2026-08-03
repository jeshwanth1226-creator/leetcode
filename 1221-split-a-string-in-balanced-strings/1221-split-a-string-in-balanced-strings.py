class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        ans = 0

        for i in s:
            if i == 'R':
                c += 1
            else:
                c -= 1

            if c == 0:
                ans += 1

        return ans
        