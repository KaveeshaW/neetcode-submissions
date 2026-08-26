class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        for num in temp:
            nums.append(num)
        return nums