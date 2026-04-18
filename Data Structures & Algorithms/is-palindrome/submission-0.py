class Solution:
    def isPalindrome(self, s: str) -> bool:
        shorts=""
        for i in s:
            if ((ord(i)>=65 and ord(i)<=90) or
                (ord(i)>=97 and ord(i)<=122) or
                (ord(i)>=48 and ord(i)<=57)):
                shorts=shorts+i.lower()
        for i in range(len(shorts)//2):
        # print(shorts)
            if shorts[i]!=shorts[len(shorts)-i-1]:
                return False
        return True