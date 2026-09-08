class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0] * 3
        for n in nums:
            colors[n] += 1
        print(colors)
        
        index = 0

        # go through the list
        for j in range(3):
            for k in range(colors[j]):
                nums[index] = j
                index += 1
        return nums