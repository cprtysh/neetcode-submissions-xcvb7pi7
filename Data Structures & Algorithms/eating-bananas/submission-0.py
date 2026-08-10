class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def tte(piles,rate,h):
            count=0
            for i in piles:
                if i%rate>0:
                    count+=i//rate +1
                else:
                    count+=i//rate
            if count<=h:
                return True
            else:
                return False

        start=1
        end= max(piles)
        ans=end
        while start<=end:
            median=(start+end)//2
            if not tte(piles,median,h):
                start=median+1
            else:
                ans=min(ans,median)
                end=median-1
        return ans
