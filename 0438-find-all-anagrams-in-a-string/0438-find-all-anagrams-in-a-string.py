class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []

        if len(p) > len(s):
            return res

        freq_p = {}
        for ch in p:
            freq_p[ch] = freq_p.get(ch, 0) + 1

        freq_w = {}
        for ch in s[:len(p)]:
            freq_w[ch] = freq_w.get(ch, 0) + 1

        if freq_w == freq_p:
            res.append(0)

        for right in range(len(p), len(s)):

            left = right - len(p)

            freq_w[s[right]] = freq_w.get(s[right], 0) + 1

            freq_w[s[left]] -= 1

            if freq_w[s[left]] == 0:
                del freq_w[s[left]]

            if freq_w == freq_p:
                res.append(left + 1)

        return res