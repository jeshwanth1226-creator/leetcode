class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split()
        p_to_s={}
        s_to_p={}
        if len(pattern)==len(s):
            for ch1,ch2 in zip(pattern,s):
                if ch1 in p_to_s:
                    if p_to_s[ch1]!=ch2:
                        return False
                p_to_s[ch1]=ch2
                if ch2 in s_to_p:
                    if s_to_p[ch2]!=ch1:
                        return False
                s_to_p[ch2]=ch1
            return True 
        return False       