class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def chrcount(a):
            arr=[0 for i in range(26)]
            for i in a:
                arr[ord(i)-97]+=1
            return tuple(arr)
        
        dmap={}
        for item in strs:
            i=chrcount(item)
            if i in dmap:
                dmap[i].append(item)
            else:
                dmap[i]=[item]
        return list(dmap.values())