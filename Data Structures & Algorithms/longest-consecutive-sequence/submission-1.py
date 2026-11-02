class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0

        # original: [0, 1, 1, 4, 3, 3, 2, 10]
        # set: [0, 1, 4, 3, 2, 10]
        # answer: 5
        # max_length: 5
        # length: 0
        # n: 0
        for n in nums:
            length = 0
            if (n - 1) not in numSet:
                while (n + length) in numSet:
                    length += 1
            max_length = max(length, max_length)
        return max_length
