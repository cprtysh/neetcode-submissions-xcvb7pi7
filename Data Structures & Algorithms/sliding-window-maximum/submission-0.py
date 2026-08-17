class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        currmax=max(nums[:k])
        left=0
        right=k
        ans=[currmax]
        while right<len(nums):
            if nums[left]==currmax:
                currmax=max(nums[left+1:right+1])
            else:
                currmax=max(currmax,nums[right])
            ans.append(currmax)
            left+=1
            right+=1
        return ans
        