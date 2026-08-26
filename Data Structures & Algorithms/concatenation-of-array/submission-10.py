class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        for num in nums:
            temp.append(num)

        for num in nums:
            temp.append(num)
        return temp