class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()
        stack.append(s[0])
        for i in range(1,len(s)):
            if len(stack)!=0 and s[i]==stack[-1]:
                stack.pop()
                continue
            stack.append(s[i])
                
        print(stack)
        return "".join(stack)