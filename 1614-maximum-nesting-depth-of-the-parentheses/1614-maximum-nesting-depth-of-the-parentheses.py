class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        par=[]
        for i in s:
            if i=='(':
                par.append('(')
                depth=max(depth,len(par))
            elif i==')':
                par.pop()
        return depth