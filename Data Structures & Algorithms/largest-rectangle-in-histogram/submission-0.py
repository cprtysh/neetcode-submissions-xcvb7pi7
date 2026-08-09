class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack=[]
        maxArea=0

        for i in range(len(heights)+1):

            currHeight = 0 if i==len(heights) else heights[i]

            while stack and currHeight<heights[stack[-1]]:

                h = heights[stack.pop()]
                if stack:
                    w = i - stack[-1] -1
                else:
                    w = i
                
                maxArea = max(maxArea, h*w)

            stack.append(i)
        return maxArea
        