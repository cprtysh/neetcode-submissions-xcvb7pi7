class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dmap={}
        for i,item in enumerate(nums):
            complement=target-item

            if complement in dmap:
                return [dmap[complement],i]
            dmap[item]=i
