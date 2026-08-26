class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) % 2 == 1):
            return False
        stack = []
        closingSymbols = [')', '}', ']']
        for symbol in s:
            if not stack and (symbol in closingSymbols):
                return False
            elif symbol == '(' or symbol == '{' or symbol == '[':
                stack.append(symbol)
                print('inside if:' + str(stack))
            elif stack and (symbol in closingSymbols):
                if symbol == ')' and stack[-1] == '(':
                    stack.pop()
                elif symbol == '}' and stack[-1] == '{':
                    stack.pop()
                elif symbol == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0