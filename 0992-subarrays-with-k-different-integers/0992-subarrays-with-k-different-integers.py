class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atmost(nums,k)-self.atmost(nums,k-1)

    def atmost(self,nums,k):
        left=0
        count=0
        freq={}
        

        for right in range(len(nums)):

                freq[nums[right]]=freq.get(nums[right],0)+1
                
                while len(freq)>k:

                    freq[nums[left]]-=1

                    if freq[nums[left]]==0:

                        del freq[nums[left]]
                    
                    left+=1
                
                count+=right-left+1
               
        return count

            

            


                
        