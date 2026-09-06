class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count=0
        def pali(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                self.count+=1
                l-=1
                r+=1
            return 
        for l in range(len(s)):
            pali(l,l+1)
            pali(l,l)
        return self.count
    