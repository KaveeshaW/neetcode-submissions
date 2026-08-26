class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0
        for number in nums:
            if(number == 1):
                count+=1
                if(max < count):
                    max = count
            if(number == 0):
                count = 0
        return max