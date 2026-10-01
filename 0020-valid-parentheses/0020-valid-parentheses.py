class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                c=stack.pop()
                if i==')':
                    if c!='(':
                        return False
                elif i=='}':
                    if c!='{':
                        return False
                elif i==']':
                    if c!='[':
                        return False
        return len(stack)==0
