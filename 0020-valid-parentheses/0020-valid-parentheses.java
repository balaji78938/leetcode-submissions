class Solution {
    public boolean isValid(String s) {
        char c[]=s.toCharArray();
        char c1[]=new char[s.length()];
        int top=0;
        for(int i=0;i<s.length();i++){
            if(c[i]=='(' || c[i]=='{' || c[i]=='[')
                c1[top++]=c[i];
            else {
                if(top==0)
                    return false;
                char ch1=c1[--top];
                if(c[i]==']' &&ch1!='[')
                        return false;
                else if(c[i]=='}'&& ch1!='{')
                        return false;
                else if(c[i]==')' && ch1!='(')
                        return false;
                
            }

        }
        return top==0;
    }
}