class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = nums + [0] * len(nums)
        i = len(nums)
        for num in nums:
            temp[i] = num
            i += 1
        return temp