class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        j=0
        i=1
        res=[]
        while i<=n and j<len(target):
            res.append("Push")
            if i==target[j]:
                j+=1
            else:
                res.append("Pop")
            i+=1
        return res