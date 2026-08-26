class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort the list
        # only one valid number exists
        # keep two pointers, one is i, the other is j
        # go through each number in an array (i) and find what number is missing
        # then go through the rest of the list (using index j) and find the other number
        # if the number does not exist, go to the next number until you find the actual number
        previousNums = {}
        for index, currentNum in enumerate(nums):
            oppositeNum = target - currentNum
            if(oppositeNum in previousNums):
                return [previousNums.get(oppositeNum), index]
            previousNums[currentNum] = index