class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:

        for i in range(len(num)-1):
            for j in range(i,len(num)):
                if num[j]==target-num[i]:
                    return [i+1,j+1]
        
        return [-1,-1]