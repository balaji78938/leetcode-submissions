class Solution {
    public int maxPalindromes(String s, int k) {
        int n=s.length();
        int ans=0,start=0;
        for(int r=k-1;r<n;r++){
            int l=r-k+1;
            if(l>=start && check(s,l,r)){
                ans++;
                start=r+1;
                continue;
            }
            l=r-k;
            if(l>=start && check(s,l,r)){
                ans++;
                start=r+1;
            }
        }
        return ans;
    }
    public boolean check(String s,int i,int j){
        while(i<j){
            if(s.charAt(i++)!=s.charAt(j--))
                return false;
        }
        return true;
    }
}