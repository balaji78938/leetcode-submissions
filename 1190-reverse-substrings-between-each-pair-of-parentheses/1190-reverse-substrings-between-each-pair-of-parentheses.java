class Solution {
    public String reverseParentheses(String s) {
        int ind=0;
        char ch[]=new char[s.length()];
        Stack<Integer> stack=new Stack<>();
        for(char c:s.toCharArray()){
            if(c=='(')
                stack.push(ind);
            else if(c==')')
                reverse(ch,stack.pop(),ind-1);
            else
                ch[ind++]=c;
        }
        return new String(ch,0,ind);
    }
    public static void reverse(char ch[],int left,int right){
        while(left<right){
            char c=ch[left];
            ch[left++]=ch[right];
            ch[right--]=c;
        }
    }
}