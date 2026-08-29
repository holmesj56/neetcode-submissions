class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        dic={}
        for r in range(len(s)):
            dic[s[r]]=dic.get(s[r],0)+1

            cur=max(dic.values())
            while (r-l+1)-cur>k :
                dic[s[l]]-=1
                l+=1
            res=max(res,(r-l+1))
        return res
                
