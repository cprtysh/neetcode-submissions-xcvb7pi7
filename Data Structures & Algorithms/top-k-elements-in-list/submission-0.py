class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map={}
        for i in nums:
            if i in map.keys():
                map[i]+=1
            else:
                map[i]=1
    
        sorted_list=sorted(map.items(),key=lambda item:-item[1])
        ans=[i for i,_ in sorted_list[:k]]
        return ans