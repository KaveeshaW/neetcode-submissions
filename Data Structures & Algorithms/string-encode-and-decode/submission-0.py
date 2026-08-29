class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans = ans + s + '€'
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        temp = ''
        for c in s:
            temp += c
            if(c == '€'):
                ans.append(temp[:-1])
                temp = ''
        return ans