class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt=[0 for i in range(26)]
        if len(s)!=len(t):
            return False
        for i in s:
            cnt[ord(i)-97]+=1
        for i in t:
            cnt[ord(i)-97]-=1
        for i in cnt:
            if i!=0:
                return False
        return True
        