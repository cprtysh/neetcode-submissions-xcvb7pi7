class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=None
        ith=None
        for i,ival in enumerate(nums):
            x=target-ival
            if x in nums[i+1:]:
                ith=i
                break
        for j,jval in enumerate(nums[ith+1:]):
            if x==jval:
                return [ith,ith+1+j]
                
