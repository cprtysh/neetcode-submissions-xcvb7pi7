class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        partsize=(len(nums1)+len(nums2)+1)//2

        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1

        left,right=0,len(nums1)
        while left<=right:
            i=(left+right)//2
            j=partsize-i

            nums1_left=-float('inf') if i==0 else nums1[i-1]
            nums1_right=float('inf') if i==len(nums1) else nums1[i]
            nums2_left=-float('inf') if j==0 else nums2[j-1]
            nums2_right=float('inf') if j==len(nums2) else nums2[j]

            if (nums1_left>nums2_right):
                right=i-1
            elif (nums2_left>nums1_right):
                left=i+1
            else:
                if (len(nums1)+len(nums2))%2:
                    return max(nums1_left,nums2_left)
                return (max(nums1_left,nums2_left)+min(nums1_right,nums2_right))/2.0