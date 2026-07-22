import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        res=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        heap=[]
        heapq.heapify(heap)
        for num , freq_num in freq.items():
            heapq.heappush(heap,(freq_num,num))
            if  len(heap)>k:
                heapq.heappop(heap)
        for freq_num,num in heap:
            res.append(num)
        return res
        

        
            


            
        
        





        



        