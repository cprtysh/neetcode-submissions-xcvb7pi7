class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in ['{','[','(']:
                st.append(i)
                continue
            if len(st):
                if i ==']' and st.pop()=='[':
                    continue
                elif i =='}' and st.pop()=='{':
                    continue
                elif i ==')' and st.pop()=='(':
                    continue
                else:
                    return False
            else:
                return False
        if len(st)>0:
            return False
        return True
            