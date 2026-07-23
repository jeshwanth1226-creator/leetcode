class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        freq_s1={}
        freq_w={}
        for i in s1:
            freq_s1[i]=freq_s1.get(i,0)+1
        for ch in s2[:len(s1)]:
            freq_w[ch]=freq_w.get(ch,0)+1
        if freq_w==freq_s1:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            left=s2[right-len(s1)]
            freq_w[s2[right]]=freq_w.get(s2[right],0)+1
            freq_w[left]-=1
            if freq_w[left]==0:
                del freq_w[left]
            if freq_w==freq_s1:
                return True
        return False


            

        



        
        