class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos=[]
        for i in range(len(speed)):
            pos.append([position[i],speed[i]])
        pos.sort(reverse=True)
        stack=[]
        for p,s in pos:
            stack.append((target-p)/s)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)