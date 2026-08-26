class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) % 2 == 1):
            return False
        stack = []
        for symbol in s:
            if symbol == '(' or symbol == '{' or symbol == '[':
                stack.append(symbol)
                print('inside if:' + str(stack))
            elif stack:
                if symbol == ')' and stack[-1] == '(':
                    stack.pop()
                elif symbol == '}' and stack[-1] == '{':
                    stack.pop()
                elif symbol == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False  
            else:
                return False
        return not stack