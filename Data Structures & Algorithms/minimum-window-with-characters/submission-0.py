class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s)<len(t):
            return ""
        count1,count2={},{}
        for i in t:
            count2[i]=count2.get(i,0)+1
        have=0
        need_count=len(count2)
        left=0
        best_len=float('inf')
        best_start=0

        for right in range(len(s)):
            c=s[right]
            count1[c]=count1.get(c,0)+1
            if c in count2 and count1[c]==count2[c]:
                have+=1
            while have==need_count:
                if right-left+1<best_len:
                    best_len=right-left+1
                    best_start=left
                d=s[left]
                count1[d]-=1
            
                if d in count2 and count2[d]>count1[d]:
                    have-=1
                left+=1
        if best_len==float('inf'):
            return ""
        return s[best_start:best_start+best_len]
        