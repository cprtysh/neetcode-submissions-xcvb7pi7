class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dmap={}
        for item in nums:
            if item in dmap:
                dmap[item]+=1
            else:
                dmap[item]=1
        h=[]
        from heapq import heapify,heappop,heappush
        heapify(h)
        for i,item in enumerate(dmap.keys()):
            if i<k:
                heappush(h,dmap[item])
            else:
                heappush(h,dmap[item])
                heappop(h)
        return [j for j,v in dmap.items() if v in h]
                