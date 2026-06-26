class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        if len(s)<k:
            return []
        seen = set()
        result = set()
        rep = 0
        # 0123456789
        # AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT
        # 9876543210
        dic = {'A':0,'C':1,'G':2,'T':3}
        for i in range(k):
            power = k - i - 1
            rep += (4**power)*dic[s[i]]
        seen.add(rep)
        for i in range(k,len(s)):
            rep -= (4**(k-1))*dic[s[i-k]]
            rep *= 4
            rep += dic[s[i]]
            if rep in seen:
                result.add(s[i-k+1:i+1])
            seen.add(rep)
        return list(result)

       