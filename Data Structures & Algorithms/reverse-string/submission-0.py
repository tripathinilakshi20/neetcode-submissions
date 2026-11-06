class Solution:
    def reverseString(self, s: List[str]) -> None:
       a=0
       n=len(s)-1
       while a<n:
        s[a],s[n]=s[n],s[a]
        a+=1
        n-=1

    