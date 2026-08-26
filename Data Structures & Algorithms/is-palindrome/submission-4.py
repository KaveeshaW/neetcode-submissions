class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newStr = ''
        # for c in s:
        #     if c.isalnum():
        #         newStr = c.lower()

        # return newStr == newStr[::1]
        sanitized_input = ''.join(char.lower() for char in s if char.isalnum())
        reversed_input = "".join(reversed(sanitized_input))
        return sanitized_input == reversed_input
        