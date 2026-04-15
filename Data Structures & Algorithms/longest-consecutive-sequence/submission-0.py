class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        max_len=0
        for i in nums:
            if i-1 not in s:
                curr_len=1
                while (i+curr_len) in s:
                    curr_len+=1
                max_len=max(max_len,curr_len)
        return max_len