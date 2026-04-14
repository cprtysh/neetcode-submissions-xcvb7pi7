class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        larr=[1 for i in range(len(nums))]
        rarr=[1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            larr[i]=larr[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            rarr[i]=rarr[i+1]*nums[i+1]
        output=[]
        for i in range(len(nums)):
            output.append(larr[i]*rarr[i])
        return output