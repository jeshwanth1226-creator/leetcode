class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            d = 1
            load = 0

            for w in weights:
                if load + w > mid:
                    d += 1
                    load = 0
                load += w

            if d <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left
        