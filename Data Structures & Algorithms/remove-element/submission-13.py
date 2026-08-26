class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tempIndexes = []
        for index in range(len(nums)):
            if(nums[index] != val):
                tempIndexes.append(nums[index])
            print(tempIndexes)

        for index in range(len(tempIndexes)):
            nums[index] = tempIndexes[index]
            print(nums)
        return len(tempIndexes)
