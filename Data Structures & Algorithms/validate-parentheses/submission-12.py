class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbolMap = {')':'(', '}':'{', ']':'['}
        for symbol in s:
            if symbol in symbolMap:
                if stack and stack[-1] == symbolMap[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        return not stack