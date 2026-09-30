class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int depth=0;
        int res[]=new int[seq.length()];
        int i=0;
        for(char c:seq.toCharArray()){
            if(c=='(')
                res[i++]=depth++%2;
            else
                res[i++]=--depth%2;
        }
        return res;
    }
}