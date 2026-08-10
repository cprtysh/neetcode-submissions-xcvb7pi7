class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b=0,len(matrix)-1
        l,r=0,len(matrix[0])-1
        while t<=b:
            midr = (t+b)//2
            if matrix[midr][l]<=target and matrix[midr][r]>=target:
                while l<=r:
                    mid= (l+r)//2
                    if matrix[midr][mid]==target:
                        return True
                    elif matrix[midr][mid]>target:
                        r=mid-1
                    else:
                        l=mid+1
            elif matrix[midr][l]>target:
                b=midr-1
            else:
                t=midr+1
        return False