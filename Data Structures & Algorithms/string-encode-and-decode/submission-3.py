class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for item in strs:
            ans += f"{len(item)}" +'#'+ item
        return ans
    
    def decode(self, j: str) -> List[str]:
        i=0
        res=[]
        digit=""
        while (i<len(j)):
            if j[i]=='#':
                #i=2,j[i]=hash,digit='10'
                if int(digit)>0:    
                    res.append(j[i+1:i+1+int(digit)])
                    i=i+1+int(digit)
                else:
                    res.append("")
                    i+=1
                digit=""
            else:
                digit+=j[i]
                i+=1
        return res   