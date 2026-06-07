class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #width=r-l so 2 pointer needed
        # maximize l*b==min(hieght[l],hieth[r]) * (r-l)
        #calc all combinations with this quantity and return max
        ans=0
        l=0
        r=len(heights)-1
        while(l<r):
            wat=min(heights[l],heights[r]) * (r-l)
            if wat>ans:
                ans=wat
            else:
                if heights[l]<=heights[r]:
                    l+=1
                else:
                    r-=1
        return ans
