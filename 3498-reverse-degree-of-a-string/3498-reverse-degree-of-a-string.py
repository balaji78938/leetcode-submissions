class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        n=len(s)
        for i in range(0,n):
            ch=ord('z')-ord(s[i])+1
            sum+=(i+1)*ch
        return sum