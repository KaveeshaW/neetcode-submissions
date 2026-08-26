class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0
        for number in nums:
            if(number == 1):
                count+=1
                if(max != 0 and max < count):
                    max = count
                elif(max == 0 and count > 0):
                    max = count
            if(number == 0):
                if(max != 0 and max < count):
                    max = count
                count = 0
        return max