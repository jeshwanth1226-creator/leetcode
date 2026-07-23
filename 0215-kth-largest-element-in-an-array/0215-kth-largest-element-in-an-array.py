import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap=[num for num in nums]
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        return heapq.heappop(heap)

        