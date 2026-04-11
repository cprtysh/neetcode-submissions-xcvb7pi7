# Given an array of integers nums and an integer target, 
# return the indices i and j such that nums[i] + nums[j] == target and i != j.
# --is given array sorted?
# --is sorting allowed?
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition
#     -- no more than 1 i,j and no less , guaranteed

# Return the answer with the smaller index first.
#     -- return such that i,j if i<j or j,i if j<i

# Input: 
# nums = [3,4,5,6], target = 7
# i!=j i=0. nums[i]=3, nums[j]=4, sum=3+4=7==target return i,j

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# i=0,j=1.  nums[i]=4, nums[j]=5, sum=4+5=9!=target
# i=0.j++,j=2, nums[i]=3, nums[j]=6, sum=4+6=10==target return i,j 

# req two indexes. i<j
# sorting may break this ordering. sorting not allowed.

# first ideas:
# iterate j completely then reset j and increment i and then iterate j completely again until all i,j pair seen
# complexity n sq. in time, constant in space.






class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sm=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sm=nums[i]+nums[j]
                if sm==target:
                    return [i,j]
        return [-1,-1]


















        