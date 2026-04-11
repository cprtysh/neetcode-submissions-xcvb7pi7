class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq 

        map={}
        for i in nums:
            if i in map.keys():
                map[i]+=1
            else:
                map[i]=1
        buckets=[[] for _ in range(len(nums)+1)]
        for q,v in map.items():
            buckets[v].append(q)
        print(buckets)
        count=0 
        ans=[]
        for i in range(len(nums),0,-1):
            if count<k:
                count+=len(buckets[i])
                ans.extend(buckets[i])
            else:
                break
        return ans
        # h=[]
        # for i,item in enumerate(map.keys()):
        #     if i<k:
        #         heapq.heappush(h,map[item])
        #     else:
        #         heapq.heappushpop(h,map[item])
        # # print(h)
        # # return h
        # ans=[k for k,v in map.items() if v in h]
        # return ans
        # sorted_list=sorted(map.items(),key=lambda item:-item[1])
        # ans=[i for i,_ in sorted_list[:k]]
        # return ans