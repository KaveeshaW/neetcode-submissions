class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = nums[:]
        for num in temp:
            nums.append(num)
        return nums