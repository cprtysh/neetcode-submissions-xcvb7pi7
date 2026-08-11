class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binS(start,end,t):
            while start<=end:
                med=(start+end)//2
                if nums[med]==target:
                    return med
                if nums[med]>target:
                    end=med-1
                else:
                    start=med+1
            return -1
        
        # if len(nums)==1:
        #     if nums[0]==target:
        #         return 0
        #     else:
        #         return -1

        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m

        if l==0:
            return binS(0,len(nums)-1,target)

        if target>=nums[0] and target<=nums[l-1]:
            return binS(0,l-1,target)
        else:
            return binS(l,len(nums)-1,target)
        
        return -1