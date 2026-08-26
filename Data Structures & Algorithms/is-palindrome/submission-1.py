class Solution:
    def isPalindrome(self, s: str) -> bool:
        # find the mid point of the string
        # if it's even, say 2, 2/2 is 1, so only process one point
        # if it's 6, 6/2 is 3,
        # if it's odd, 1/2 is 0, then yes it is a palindrom
        # 3/2 is 1, ignore middle character
        # store what the first half of the string was
        # go through reverse from the other half, if it is the same then return true
        # otherwise return false
        sanitized_input = ''.join(char.lower() for char in s if char.isalnum())
        reversed_input = "".join(reversed(sanitized_input))
        return sanitized_input == reversed_input
        # print(sanitized_input)
        # print(len(sanitized_input))
        # half_length = len(sanitized_input) // 2
        # # print(half_length)
        # if(half_length % 2 == 0):
        #     print(sanitized_input[0:half_length])
        #     print("".join(reversed(sanitized_input)))
        #     return True
        #     # return sanitized_input[0:half_length] == sanitized_input[len(sanitized_input) - 1: half_length - 1]
        # else:
        #     return False
        