class Solution:
    def isValid(self, s: str) -> bool:
        openSymbols = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for symbol in s:
            if symbol in closeToOpen:
                if openSymbols and openSymbols[-1] == closeToOpen[symbol]:
                    openSymbols.pop()
                else:
                    return False
            else:
                openSymbols.append(symbol)
        return len(openSymbols) == 0