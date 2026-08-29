class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        dic={}
        l=0
        dic[s[0]]=1
        res=1
        for i in range(1,len(s)):
            dic[s[i]] = dic.get(s[i],0)+1
            while dic[s[i]] >1 :
                dic[s[l]]-=1
                l+=1
            res=max(res,i-l+1)
        return res

