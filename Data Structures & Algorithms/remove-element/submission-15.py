class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valPointer = 0
        for index in range(len(nums)):
            if(nums[index] != val):
                nums[valPointer] = nums[index]
                valPointer+=1

        return valPointer
