class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans=[0] * len(temp)
        stack=[]
        for i,t in enumerate(temp):
            while stack and t>stack[-1][0]:
                st,si=stack.pop()
                ans[si]=i-si
            stack.append([t,i])
        return ans
