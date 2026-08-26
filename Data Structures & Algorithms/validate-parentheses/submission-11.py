class Solution:
    def isValid(self, s: str) -> bool:
        openingSymbols = ['(', '{', '[']
        if(len(s) % 2 == 1 or s[0] not in openingSymbols):
            return False
        stack = []
        closingSymbols = [')', '}', ']']
        for symbol in s:
            if symbol == '(' or symbol == '{' or symbol == '[':
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