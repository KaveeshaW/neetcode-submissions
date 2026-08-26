class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        for iterations in range(2):
            for num in nums:
                temp.append(num)
        return temp