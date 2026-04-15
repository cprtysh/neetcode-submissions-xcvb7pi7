class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        dmap={')':'(',']':'[','}':'{'}
        for i in s:
            if i in dmap:
                if st and st[-1] == dmap[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)

        return True if not st else False
            