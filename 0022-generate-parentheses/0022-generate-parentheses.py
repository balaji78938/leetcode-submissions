class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def backtrack(ans,res,open,close,n):
            if len(ans)==2*n:
                return res.append(ans)
                
            if open<n:
                backtrack(ans+'(',res,open+1,close,n)
            if close<open:
                backtrack(ans+')',res,open,close+1,n)
        backtrack("",res,0,0,n)
        return res
        