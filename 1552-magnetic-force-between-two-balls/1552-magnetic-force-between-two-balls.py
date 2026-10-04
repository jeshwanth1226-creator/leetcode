class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        left=1
        right=max(position)

        while left<=right:
            mid=(left+right)//2

            balls = 1
            last = position[0]

            for p in position[1:]:
                if p - last >= mid:
                    balls += 1
                    last = p

            if balls>=m:
                left=mid+1
            else:
                right=mid-1

        return right





